from django.db import models

# Create your models here.


class User(models.Model):
	userid = models.CharField(max_length=200)
	real_name = models.CharField(max_length=200)
	tz = models.CharField(max_length=200)


class ActivityPeriod(models.Model):
	start_time = models.CharField(max_length=200)
	end_time = models.CharField(max_length=200)
