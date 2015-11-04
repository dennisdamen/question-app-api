# -*- coding: utf-8 -*-

# Third party
from rest_framework import filters
from .models import Subject
from django.db.models import Q


class IsUserSubjectsOnlyFilter(filters.BaseFilterBackend):
	def filter_queryset(self, request, queryset, view):
		return Subject.objects.filter(Q(owner=request.user) | 
                               		  Q(receiver=request.user))

class IsUserQuestionsOnlyFilter(filters.BaseFilterBackend):
	def filter_queryset(self, request, queryset, view):
		return queryset.filter(owner=request.user)


class IsUserNextActionOnly(filters.BaseFilterBackend):
	def filter_queryset(self, request, queryset, view):
		return queryset.filter(next_action=request.user)