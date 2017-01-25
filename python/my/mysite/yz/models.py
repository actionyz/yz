from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserInfo(models.Model):
	user = models.CharField(max_length = 32)
	pwd  = models.CharField(max_length = 32)
class person(models.Model):
	user = models.CharField(max_length = 32)
	pwd  = models.CharField(max_length = 32)
class college(models.Model):
	user = models.CharField(max_length = 32)
	pwd  = models.CharField(max_length = 32)