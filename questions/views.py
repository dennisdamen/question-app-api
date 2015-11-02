from django.shortcuts import render
from questions.models import Subject
from questions.models import Question
from questions.serializers import QuestionSerializer
from questions.serializers import SubjectSerializer
from questions.serializers import UserSerializer
from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from questions.permissions import IsOwnerOrReadOnly

class SubjectList(	generics.ListCreateAPIView):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class QuestionList(generics.ListCreateAPIView):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
