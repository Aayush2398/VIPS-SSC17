from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.home,name='home'),
    url(r'^logout/$', views.logout,name='logout'),
    url(r'^events/$', views.get_events, name='events'),
    url(r'^profile/$', views.fetch_profile, name='profile'),
    url(r'^validate_team/$', views.validate_team, name='validate_team'),
    url(r'^join_team/$', views.join_team, name='join_team'),
    url(r'^join_team_dhwanit/$', views.join_team_dhwanit, name='join_team_dhwanit'),
    #url(r'^generate_report/$', views.generate_report, name='generate_report'),
    url(r'^generate_report/(?P<code>[\w.@+-]+)/$', views.generate_report, name='generate_report'),
   
    
]

