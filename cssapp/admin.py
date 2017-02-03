from django.contrib import admin
from .models import Event, Volunteer, Participant, Team, CampusAmbassador,Winners

from django.contrib.admin.models import LogEntry, DELETION
from django.utils.html import escape
from django.core.urlresolvers import reverse

admin.site.site_title = 'CSI - State Students Convention'
admin.site.site_header = 'CSI - State Students Convention'

# Register your models here.
admin.site.register(CampusAmbassador)
#admin.site.register(Student)
#admin.site.register(Volunteer)
#admin.site.register(Team)

class VolunteerAdmin(admin.ModelAdmin):
	list_display = ('name','event','contact_number','enrollment_number','course','section','val')


class EventAdmin(admin.ModelAdmin):
	list_display = ('code','name','has_started','has_ended','venue','teacher_incharge')

class CampusAdmin(admin.ModelAdmin):
	list_display = ('name','enrollment_number','sponsors','ref_code')

class WinnerAdmin(admin.ModelAdmin):
	list_display = ('name','college','position','event')


class StudentAdmin(admin.ModelAdmin):


	def get_queryset(self,request):
		qs = super(StudentAdmin, self).get_queryset(request)
		
		user = request.user
		group = request.user.groups.values_list('name', flat=True).first()

		if group:
			obj=Event.objects.filter(name=group) #name of group same as name of event
			
			return qs.filter(event_name=obj)

		else:
			return qs.all()

	# Non Super users do not have permission to do anything except reading data
	def changelist_view(self, request, extra_context=None):
		if not request.user.is_superuser:
			self.list_display = ('student_name','college','contact_number','event_name','team_name','email_id','is_csi_member','paid','category','song_name')
			#self.list_display_links = None
			return super(StudentAdmin, self).changelist_view(request, extra_context)
		else:
			self.list_display = ('student_name','college','contact_number','event_name','team_name','email_id','is_csi_member','paid','category','song_name')
			self.list_editable = ('paid',)
			return super(StudentAdmin, self).changelist_view(request, extra_context)

	
	#list_display = ('student_name','college','contact_number','event_name','team_name','is_csi_member','paid',)
	#search_fields = ['event_name__name','team_name__team_name','contact_number',]
	

	list_display = ('student_name','college','contact_number','event_name','team_name','is_csi_member','paid')
	search_fields = ['event_name__name','contact_number','team_name__team_name','student_name']

	
class TeamAdmin(admin.ModelAdmin):
	list_display = ('team_name','team_pass','event_name','team_leader')

	def event_name(self,obj):
		return obj.event_name.name
	def team_leader(self,obj):
		return obj.created_by.username



class LogEntryAdmin(admin.ModelAdmin):

	date_hierarchy = 'action_time'
	#readonly_fields = LogEntry._meta.get_fields()

	list_filter = ['user', 'content_type', 'action_flag']

	search_fields = ['object_repr','change_message']

	list_display = ['action_time','user','content_type','object_link','action_flag','change_message',]



	def has_add_permission(self, request):
		return False


	def has_change_permission(self, request, obj=None):
		return request.user.is_superuser and request.method != 'POST'


	def has_delete_permission(self, request, obj=None):
		return False


	def object_link(self, obj):
		if obj.action_flag == DELETION:
			link = escape(obj.object_repr)
		else:
			ct = obj.content_type
			link = u'<a href="%s">%s</a>' % (
				reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
				escape(obj.object_repr), 
				)
		return link


		object_link.allow_tags = True
		object_link.admin_order_field = 'object_repr'
		object_link.short_description = u'object'


		def queryset(self, request):
			return super(LogEntryAdmin, self).queryset(request) \
			.prefetch_related('content_type')



admin.site.register(LogEntry, LogEntryAdmin)


admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Participant, StudentAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Winners,WinnerAdmin)





