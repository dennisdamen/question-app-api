from rest_framework import serializers
from questions.models import Subject
from questions.models import Question
from django.contrib.auth.models import User

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = ('id', 'created', 'lastEdited', 'content', 'owner', 'subject')

class SubjectSerializer(serializers.ModelSerializer):
	questions = QuestionSerializer(many=True, read_only=True)

	class Meta:
		model = Subject
		fields = ('id', 'title', 'questions', 'created', 'lastEdited')

class UserSerializer(serializers.ModelSerializer):
	subjects = serializers.PrimaryKeyRelatedField(many=True, queryset=Subject.objects.all())
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'subjects', 'owner')