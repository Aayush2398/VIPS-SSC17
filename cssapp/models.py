from __future__ import unicode_literals
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone
import uuid


# Create your models here.

class Event(models.Model):

	code = models.CharField(primary_key=True, max_length=20)
	name = models.CharField(max_length=200)
	event_header = models.CharField(max_length=100)
	event_details = models.TextField()
	time = models.CharField(max_length=100)
	venue = models.CharField(max_length=100)
	teacher_incharge = models.CharField(max_length=300)
	has_started = models.BooleanField(default=False)
	has_ended = models.BooleanField(default=False)
	image_url = models.CharField(max_length=100)
	


	def __str__(self):
		return self.name


class Volunteer(models.Model):

	event = models.ForeignKey('Event')
	name = models.CharField(max_length=30)
	enrollment_number = models.BigIntegerField(primary_key=True)
	course_choices = (('a','BCA'),('b','MCA'))
	course = models.CharField(max_length=1, choices=course_choices)
	section_choices = (('a','Morning A'),('b','Morning B'),('c','Morning C'),('d','Evening A'),('e','Evening B'))
	section = models.CharField(max_length=1,choices=section_choices)
	email = models.EmailField(unique=True)
	contact_number = models.BigIntegerField()
	val = models.CharField(max_length=2)


	def __str__(self) :
		return self.name


class Team(models.Model):

	class Meta:
		unique_together = (('created_by','event_name'),)

	created_by = models.ForeignKey('auth.User')
	team_name = models.CharField(max_length=100)
	dhwanit_category = (('a','Indian Vocal Solo'),('b','Western Vocal Solo'),('c','Intrumental Solo'),('d','Group Musical'))
	category = models.CharField(max_length=1,choices=dhwanit_category, blank=True, null=True)
	team_pass = models.CharField(max_length=100)
	event_name = models.ForeignKey('Event')
	email_id = models.EmailField()


	def __str__(self):
		return self.team_name

class Participant(models.Model):

	class Meta:
		unique_together = (('email_id','event_name','student_name'),)
	
	team_name = models.ForeignKey('Team', blank=True, null=True)
	event_name = models.ForeignKey('Event')
	dhwanit_category = (('a','Indian Vocal Solo'),('b','Western Vocal Solo'),('c','Intrumental Solo'),('d','Group Musical'))
	category = models.CharField(max_length=1,choices=dhwanit_category, blank=True, null=True)
	student_name = models.CharField(max_length=50)
	college = models.CharField(max_length=100, blank=False)
	year = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
	course = models.CharField(max_length=30, blank=False)
	email_id = models.EmailField(max_length=69)
	contact_number = models.BigIntegerField()
	song_name = models.CharField(max_length=300, default="Not Valid")
	ref_code = models.CharField(max_length=50,blank=True)
	is_csi_member = models.BooleanField(default=False)
	paid = models.BooleanField(default=False)
	event_ref=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)


	def __str__(self):
		return self.student_name


class CampusAmbassador(models.Model):

	name = models.CharField(max_length=60)
	enrollment_number = models.BigIntegerField(primary_key = True)
	sponsors = models.TextField()
	ref_code = models.PositiveIntegerField(unique=True)

	def __str__(self):
		return self.name


class Colleges(models.Model):

	name = models.CharField(max_length=200)
	enrollment_number= models.BigIntegerField(primary_key=True)
	visited_by = models.CharField(max_length=50)
	visited_on = models.DateTimeField()
	note = models.TextField(blank=True, null=True)


class Winners(models.Model):

	name = models.CharField(max_length=100)
	college = models.CharField(max_length=200)
	event = models.ForeignKey('Event')
	position = models.PositiveIntegerField()

	def __str__(self):
		return self.name
