from django.db import models

class User(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=30)


	class Meta:
		ordering = ('created',)