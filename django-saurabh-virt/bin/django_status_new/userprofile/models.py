#from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	like_cheese = models.BooleanField(default=True)
	favourite_hamster_name = models.CharField(max_length=50)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])



