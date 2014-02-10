from django.conf.urls import patterns, include, url
from privacy import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<p_id>\d+)/$', views.policy, name='policy'),
	url(r'^authority/$', views.authority, name='authority')
)
