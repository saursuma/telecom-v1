from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Persons(models.Model):
	title = models.TextField(max_length=254)
	body = models.TextField()
	#pub_date=models.DateTimeField('date_published')
	likes= models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.title

class Comments(models.Model):
	article = models.ForeignKey(Persons)
	text = models.TextField()
