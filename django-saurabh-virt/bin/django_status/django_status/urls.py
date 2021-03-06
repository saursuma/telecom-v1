"""django_status URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns, include
from django.contrib import admin
admin.autodiscover()

##from persons.views import HelloTemplate

##urlpatterns = [
  ##  url(r'^admin/', include(admin.site.urls)),
  ##  url(r'^polls/', include('persons.urls' , namespace="persons")),
 ##   url(r'^hello/$' , persons.views.hello),
##]


urlpatterns = patterns('',
		(r'^persons/' , include('persons.urls')),
		(r'^admin/' , include(admin.site.urls)),
#user auth urls
		url(r'^accounts/login/$' , 'django_status.views.login'),
		url(r'^accounts/auth/$' , 'django_status.views.auth_view'),
		url(r'^accounts/logout/$' , 'django_status.views.logout'),
		url(r'^accounts/loggedin/$' , 'django_status.views.loggedin'),
		url(r'^accounts/invalid/$' , 'django_status.views.invalid_login'),
url(r'^accounts/register/$' , 'django_status.views.register_user'),
		url(r'^accounts/register_success/$' , 'django_status.views.register_success'),
##		url(r'^persons/$' , 'persons.views.persons'),
##		url(r'^$' , 'django_status.views.home'),
##		url(r'^hello_template/$' , 'persons.views.hello_template'),
##		url(r'^hello_template_simple/$' , 'persons.views.hello_template_simple'),
##		url(r'^hello_class_view/$' , HelloTemplate.as_view()),

)

