from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, UserManager
from rest_framework.authtoken.models import Token
from django.conf import settings


class UserManager(UserManager):
	def create_user(self, *args, **kwargs):
		"""
		Creates and saves a User with the given email, date of
		birth and password.
		"""
		if not email:
		    raise ValueError('Users must have an email address')

		user = self.model(
		    email=self.normalize_email(email),
		    date_of_birth=date_of_birth,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, date_of_birth, password):
		"""
		Creates and saves a superuser with the given email, date of
		birth and password.
		"""
		user = self.create_user(email,
		    password=password,
		    date_of_birth=date_of_birth
		)
		user.is_admin = True
		user.save(using=self._db)
		return user


class User(AbstractUser):
	pass

class Subject(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	lastEdited = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='subjects')

	# Receiver is the user who receives the question and get access to this subject (visible)
	receiver = models.ForeignKey(settings.AUTH_USER_MODEL)

	# A question can be resolved when its answered, this boolean will tell if it is
	resolved = models.BooleanField(default=False)

	# Determines the next action
	next_action = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='next_actions')

	class Meta:
		ordering = ('-lastEdited',)


# Added myself, needs reviewing:
class Question(models.Model):
	subject = models.ForeignKey(Subject, related_name='questions')
	created = models.DateTimeField(auto_now_add=True)
	lastEdited = models.DateTimeField(auto_now_add=True)
	content = models.CharField(max_length=100)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL)
	# answerer = models.ForeignKey('User')
	# answered = BooleanField(initital=True)

	class Meta:
		ordering = ('-created',)




@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)