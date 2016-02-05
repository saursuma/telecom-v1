from __future__ import unicode_literals

from django.db import models
from time import time

def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

# Create your models here.

class Persons(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
   # role = models.CharField(max_length=1, choices=(('M', ('Manager')), ('I', ('Developer')))
    email = models.CharField(max_length=254, null=True)
    address = models.CharField(max_length=254, null=True)
    birthdate = models.DateField(null=True)
    city = models.CharField(max_length=60, null=True)
    like = models.IntegerField(null=True)
    state_province = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=50, null=True)
    website = models.URLField(null=True)
    thumbnail = models.FileField(upload_to=get_upload_file_name)
    
    def __unicode__(self):
        return self.first_name
#    def __unicode__(self):
#		return self.first_name

#    def get_absolute_url(self):
#        	return "/persons/get/%i/" % self.id
    def get_absolute_url(self):
      return "/persons/get/%i/" % self.id 
    def get_full_name(self):
      return '%s %s' % (self.first_name, self.last_name)      


class Task(models.Model):
	person = models.ForeignKey(Persons)
	description = models.CharField(max_length=254, default='Dummy')
	TaskInitiator= models.CharField(max_length=254, null=True)
	actualOwner = models.CharField(max_length=254, null=True)
	TaskStatus = models.CharField(max_length=254, null=True)
	TaskPriority = models.CharField(max_length=254, null=True)
	CreatedOn = models.CharField(max_length=254, null=True)
	CreatedBy = models.CharField(max_length=254, null=True)
	CompletedOn = models.CharField(max_length=254, null=True)
	CompletedBy = models.CharField(max_length=254, null=True)
	TaskType = models.CharField(max_length=254, null=True)

def __unicode__(self):
		return self.TaskStatus
class Comment(models.Model):
	person = models.ForeignKey(Persons, default=1)
	task = models.ForeignKey(Task)
	description = models.CharField(max_length=254, null=True)
	CreatedOn = models.CharField(max_length=254, null=True)
	CreatedBy = models.CharField(max_length=254, null=True)
	TaskType = models.CharField(max_length=254, null=True)



 

