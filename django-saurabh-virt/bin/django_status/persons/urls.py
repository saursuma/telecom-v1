from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^all/$', 'persons.views.persons'),
	url(r'^get/(?P<person_id>\d+)/$', 'persons.views.person'),
	url(r'^language/(?P<language>[a-z\-]+)/$', 'persons.views.language'),
	url(r'^create/$', 'persons.views.create'),
)

