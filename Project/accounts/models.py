from django.db import models

class UserProfile(models.Model):
	first_name=models.CharField(max_length=30)
	middle_name=models.CharField(max_length=30, blank=True)
	last_name=models.CharField(max_length=30)
	user_name=models.CharField(max_length=30, unique=True)
	description=models.CharField(max_length=200, default='', blank=True)
	age=models.PositiveIntegerField()
	email=models.EmailField()
	website=models.URLField(blank=True)
	phone=models.PositiveIntegerField()

	def __str__(self):
		return self.user_name


