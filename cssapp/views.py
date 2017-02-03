from django.shortcuts import render
from django.shortcuts import render, get_object_or_404 
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
from django.core.mail import EmailMultiAlternatives
import sendgrid
import os
from django.core.exceptions import SuspiciousOperation
from sendgrid.helpers.mail import *
from .models import Event, Participant, Team,Volunteer
from django.core.mail import EmailMessage
from django.db.models import Count

# Create your views here.


BLACK_LIST = ['UdItMiTtal']  # add FB IDs of annoying users here :)

#method to send confirmatuion using ACE ID
def send_confirmation_mail(user_email, event,ID, name):

	msg = EmailMessage('Registration Confirmation',
                       'Hey %s,<br><br>Welcome to State Students Convention,2017 in association with Computer Society of India.Your registration is confirmed for %s.Your reg ID is %s .<br>General Instructions<br>1.One time registration fees for the event is Rs.100(Non CSI members) and Rs.60(CSI Members) payable at the main counter.<br>2.Registration fee includes Food Coupons.<br>3.The above mentioned charges are NOT applicable for students participating in any of the following events:<br><br>-Paper Presentation<br>-Dance<br>-Music<br>-Nukad Natak<br>-Appathon<br>-Console Gaming<br>-Lan Gaming<br><br>4.Separate registration fees and instructions have been provided in the rule book for registration in the events listed above.<br>Let us know if you have any queries.<br><br>Best of Luck!<br><br>Regards,<br>Team ACE'%(name,event,ID),
                       'vips.ace@gmail.com',
                       [user_email]
                  )

	msg.content_subtype = "html"
	response = msg.send()

	return response


# method to send confirmation emails to participants for their registeration using sendGrid API
def send_confirmation(user_email,event,ID, name):

	sg = sendgrid.SendGridAPIClient(apikey=os.environ['SENDGRID_API_KEY'])
	
	from_email = Email("Admin@vipsace.org")
	subject = "SSC Registeration"
	to_email = Email(user_email)

	body_text = 'You have successfully registered for %s and your reference id is%s '%(event,ID) 

	content = Content("text/plain", body_text)
	mail = Mail(from_email, subject, to_email, content)
	response = sg.client.mail.send.post(request_body=mail.get())

	return response.status_code  # 202 if msg is sent and delivered


def send_team_code(user_email, team_leader, ID, event_name):
	
	msg = EmailMessage('Team Registeration','Hey %s,<br><br>Welcome to State Students Convention,2017 organized by Computer Society of India.<br>We have registered your team for %s.Your team code is %s.Please do not share it with anyone other than your team mates.Also you will have to use this team code to add yourself to the team by clicking on Join Team button and filling required details.Once you add yourself you can share this code with your team mates.<br>Best of luck<br><br>Regards,<br>Team ACE'%(team_leader,event_name,ID),
        'vips.ace@gmail.com',
        [user_email]
       )

	msg.content_subtype = "html"
	response = msg.send()
	return response


#Landing page of web app
def index(request):
	
	if request.user.is_active:
		user = User.objects.get(username=request.user)
		
		if user in BLACK_LIST:
			auth_logout(request)
			return redirect('/')

		
		return redirect('/home')


	#events = Event.objects.all()   # use it if u want to load the event data dynamicaly

	return render(request, 'cssapp/index.html',{})

@login_required(login_url='/')
def home(request):
	
	user = User.objects.get(username=request.user)
	name = user.get_full_name()
	
	print "Current User : " + str(name)
	
	return render(request, 'cssapp/home.html')


def logout(request):
	auth_logout(request)
	return redirect('/')


@login_required(login_url='/')
def get_events(request):

	events = Event.objects.all()

	return render(request,'cssapp/events.html',{'events':events})


#method to fetch user profile information
@login_required(login_url='/')
def fetch_profile(request):

	participant = User.objects.get(username=request.user)
	email_id = participant.email

	data = Participant.objects.filter(email_id=email_id)

	return render(request,'cssapp/profile.html',{'data':data,'user':participant.get_full_name})

	
# Test if team already exists , if not user can use that name to create his/her team
@csrf_exempt
def validate_team(request):
	
	if request.method != "POST":
		raise SuspiciousOperation("Illegal request; This is event is reported and you will be blocked from any further access to this website")
	
	team = request.POST.get('team', None) 
	user = User.objects.get(username=request.user)
	code = request.POST.get('code', None)
	event = request.POST.get('event',None)
	email = request.POST.get('email',None)
	catg = request.POST.get('catg',None)
	print team,user,code,event,email,catg
	team = team.upper()
	#code = code.upper()
	team_leader = user.get_full_name()

	category_dict = { 'Indian Vocal Solo ' : 0 , 'Western Vocal Solo':1, 'Instrumental Solo':2,'Group Musical':3, None:None}
	catg_choice = Participant.dhwanit_category

	# because one team per user per event is allowed
	event_obj = Event.objects.get(name=event)
	is_taken = Team.objects.filter(created_by=user).filter(event_name=event_obj).exists() or Team.objects.filter(team_pass=code).exists()#returns true if logged in user has already created a team
	if is_taken:
		data = {'is_taken':is_taken}
		return JsonResponse(data)


	# If team doesn't already exist, allow user to create one
	if not is_taken :

		#participant cannot register with null value of code
		if team and code:			
			does_exist = Team.objects.filter(team_name=team).filter(team_pass=code).exists() # returns true of team and code pair already exists
			if not does_exist and catg:
				team_obj = Team(team_name=team, team_pass = code ,created_by = user, event_name=event_obj,category=catg_choice[category_dict[str(catg)]][0])
				team_obj.save() # Team leader is not added untill he submits his details in join team module
				response = send_team_code(email, team_leader, code, event)
				if response:
					print "added and mail sent"

			if not does_exist and not catg:
				team_obj = Team(team_name=team, team_pass = code ,created_by = user, event_name=event_obj,category=None)
				team_obj.save() # Team leader is not added untill he submits his details in join team module
				response = send_team_code(email, team_leader, code, event)
				if response:
					print "added and mail sent"

		else:
			is_taken = True


		data = {'is_taken': is_taken}
	
		return JsonResponse(data)
#method to register particpant in an event
def registerParticipant(name, college, year, course, contact, email, event_obj, team_obj):

	try:
		#Test whether participant has already registered for this event
		has_registered = Participant.objects.filter(event_name=event_obj).filter(student_name=name).exists()
		if not has_registered:
			p_obj = Participant(team_name=team_obj, event_name=event_obj, student_name=name, college=college, year=year,contact_number=contact, email_id=email, course=course)
			p_obj.save()
			return True
			
	except:
	
		return False
		

#method to allow participant to join existing team using team code
@csrf_exempt
def join_team(request):

	#Option 1: Join an existing team
	#Option 2 : Register as an individual

	if request.method != "POST":
		raise SuspiciousOperation("Illegal request; This event is reported and you will be blocked from any further access to this website")

	code = request.POST.get('team', None)
	event = request.POST.get('event', None)
	email = request.POST.get('email', None)
	course = request.POST.get('course',None)
	contact = request.POST.get('contact',None)
	college = request.POST.get('college',None)
	year = request.POST.get('year', None)

	required = {'email':email, 'course':course, 'college':college, 'year':year,'contact':contact}
	for key in required:
		if not required[key]:
			
			data = {'status': '%s Field is required'%key}
			return JsonResponse(data)

	user = User.objects.get(username=request.user)
	name = user.get_full_name()
	print(code,event,email,course,contact,college,year,name)

##***************************************Individual Registeration*****************************************************##


	if not code :
		#This means user wants to register for solo participation
		event_obj = Event.objects.get(name=event) # store event object in event variable
		#Test if user is already registered for this event
		has_registered = Participant.objects.filter(event_name=event_obj).filter(student_name=name).exists()
		if not has_registered:
			p_obj = Participant(event_name=event_obj, student_name=name, college=college, year=year,contact_number=contact, email_id=email, course=course)
			p_obj.save()
			print "Added"
			#Now fetch computer generated ID for this record
			q_obj = Participant.objects.filter(email_id=email).filter(event_name=event_obj).filter(student_name=name)
			ID = q_obj[0].event_ref  # fetch ID
			# And send it to participant's email ID
			status = send_confirmation_mail(email, event_obj.name, ID, name) # General email format
			if status :
				#if status is true mail has been sent
				data = {'status':"Your registeration is confirmed.Please check your email inbox"}
				print "added and mail sent"
				return JsonResponse(data)

		else:
			data = { 'status': "You have already registered for this event" }
			return JsonResponse(data)


##***************************************Registeration using Team Code**************************************************************##

	if code :
		# first of all test whether the team exist or not
		does_exist = Team.objects.filter(team_pass=code).exists() # returns true if team code exists
		event_obj = Event.objects.get(name=event) # store event object in event variable

	
		status = 0  #default value
		success=False #default value

		if does_exist:
			try:
				team_obj = Team.objects.get(team_pass=code)
			except:
				data = {'status': 'We are Sorry this is not allowed :/.'}
				return JsonResponse(data)
	
			success = registerParticipant(name, college, year, course, contact, email, event_obj, team_obj)
			#print(success)


			if success :
				q_obj = Participant.objects.filter(email_id=email).filter(event_name=event_obj).filter(student_name=name)
				ID = q_obj[0].event_ref  # fetch ID
				#print(q_obj)
				status = send_confirmation_mail(email, event_obj.name, ID, name)
				print "added and mail sent"

##*************************************Confirmation Logic(Team Registeration)*******************************************##

		if success and status :
			status = "Registeration Confirmed. Please check your email"
			print "mail sent"
		if success and not status:
			status = "Registeration Confirmed but we were unable to send you confirmation email"
		if not success :
			status = "You have already registered for this event.See you soon."
		if not does_exist:
			status = "Invalid Team Code"

		data = { 'status': status }

		return JsonResponse(data)


#####*****************************************Generate Real Time Reports****************************************************##*
#TODO
#method to generate event wise reports in real time 
@csrf_exempt
def generate_report(request, code):

	event = Event.objects.get(code=code)
	reg_count = Participant.objects.filter(event_name=event).count()
	attendees = Participant.objects.filter(event_name=event,paid=True).count()
	colleges = Participant.objects.filter(event_name=event).annotate(Count('college', distinct=True))

	teams = Team.objects.filter(event_name=event).count()
	try:
		winners = Winners.objects.filter(event=code)
	except:
		winners = []

	studentVolunteers = Volunteer.objects.filter(event=event)
	student_volunteer=[]
	college_list = []
	college_set = []
	winner_dict = {}

	for student in studentVolunteers:
		student_volunteer.append(student.name)
	
	for college in colleges:
		college_list.append(college.college)
	
	college_list = map(lambda x:x.upper(),college_list)


	college_list = map(lambda x:x.upper(),college_list)
	college_list = set(college_list)


	for college in college_list:
		college_set.append(college)

	for winner in winners:
		winner_dict[str(winner.position)] = [winner.name,winner.college]


	data = {'name':event.name, 
            'description':event.event_details,
            'registrations': reg_count,
            'attendees': attendees,
            'studentVolunteers': student_volunteer,
            'techerIncharge': event.teacher_incharge,
            'venue':event.venue,
            'teams': teams,
            'winners':winner_dict,
            'colleges': college_set
            }


	return JsonResponse(data)




	# Count total number of Partipants 

	# Number of registerations
	# Number of attendees 
	# Winners
	# Event Description
	# Event duration (expected)
	# mkdir event_name
	# copy data to exel
	# copy data to exel

@csrf_exempt
def join_team_dhwanit(request):

	catg = request.POST.get('catg', None)
	event = request.POST.get('event', None)
	email = request.POST.get('email', None)
	course = request.POST.get('course',None)
	contact = request.POST.get('contact',None)
	college = request.POST.get('college',None)
	year = request.POST.get('year', None)

	user = User.objects.get(username=request.user)
	name = user.get_full_name()

	category_dict = { 'Indian Vocal Solo' : 0 , 'Western Vocal Solo':1, 'Instrumental Solo':2,'Group Musical':3}

	print(event,email,course,contact,college,year,name,catg)


	event_obj = Event.objects.get(name=event)
	catg_choice = Participant.dhwanit_category
	has_registered = Participant.objects.filter(event_name=event_obj).filter(student_name=name).exists()
	if not has_registered:
		p_obj = Participant(event_name=event_obj, student_name=name, college=college, year=year,contact_number=contact, email_id=email, course=course,category=catg_choice[category_dict[str(catg)]][0])
		p_obj.save()
		print "Added"
			#Now fetch computer generated ID for this record
		q_obj = Participant.objects.filter(email_id=email).filter(event_name=event_obj).filter(student_name=name)
		ID = q_obj[0].event_ref  # fetch ID
			# And send it to participant's email ID
		status = send_confirmation_mail(email, event_obj.name, ID, name) # General email format
		if status :
				#if status is true mail has been sent
			data = {'status':"Your registeration is confirmed.Please check your email inbox"}
			return JsonResponse(data)

	else:
		data = { 'status': "You have already registered for this event" }
		return JsonResponse(data)


