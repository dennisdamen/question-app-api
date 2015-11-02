from django.db import models

class Subject(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	lastEdited = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100)
	question = models.CharField(max_length=255)
	owner = models.ForeignKey('auth.User', related_name='subjects')


	class Meta:
		ordering = ('-lastEdited',)

# Added myself, needs reviewing:
class Question(models.Model):
	subject = models.ForeignKey(Subject, related_name='questions')
	created = models.DateTimeField(auto_now_add=True)
	lastEdited = models.DateTimeField(auto_now_add=True)
	content = models.CharField(max_length=100)
	owner = models.ForeignKey('auth.User')
	# answerer = models.ForeignKey('User')
	# answered = BooleanField(initital=True)

	class Meta:
		ordering = ('-created',)

# class Friends(models.Model):
# 	users = models.ManyToMany(User, related_name='friends')