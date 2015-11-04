from rest_framework import serializers
from questions.models import Subject
from questions.models import Question
from django.contrib.auth.models import User


class QuestionSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		instance = super(QuestionSerializer, self).create(validated_data)
		user = self.context['request'].user
		subject = instance.subject
		instance.subject.next_action = (subject.owner 
										if user == subject.receiver else subject.receiver)
		return instance

	def validate_subject(self, subject):
		if self.context['request'].user in set([subject.owner, subject.receiver]):
			return subject
		raise serializers.ValidationError('You cannot create an answer to a question you are not assigned to')

	class Meta:
		model = Question
		fields = ('id', 'created', 'lastEdited', 'content', 'owner', 'subject')
		read_only_fields = ('id', 'created', 'lastEdited', 'owner')


class SubjectSerializer(serializers.ModelSerializer):
	questions = QuestionSerializer(many=True, read_only=True)

	def create(self, validated_data):
		validated_data['next_action'] = validated_data.get('receiver', None)
		return super(SubjectSerializer, self).create(validated_data)

	class Meta:
		model = Subject
		fields = ('id', 'title', 'questions', 'created', 'lastEdited', 
				  'owner', 'receiver')
		write_only_fields = ('receiver', )
		read_only_fields = ('created', 'lastEdited', 'owner')


class UserSerializer(serializers.ModelSerializer):
	subjects = serializers.PrimaryKeyRelatedField(many=True, queryset=Subject.objects.all())
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'subjects', 'owner')