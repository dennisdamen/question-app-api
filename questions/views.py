from questions.models import Subject, Question, User
from questions.serializers import QuestionSerializer
from questions.serializers import SubjectSerializer
from rest_framework.decorators import list_route
from questions.serializers import UserSerializer
from rest_framework import mixins, viewsets
from rest_framework import permissions
from questions.permissions import IsOwnerOrReadOnly
from .filters import IsUserQuestionsOnlyFilter, IsUserSubjectsOnlyFilter, IsUserNextActionOnly


class QuestionViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin,
					  viewsets.GenericViewSet):
	serializer_class = QuestionSerializer
	queryset = Question.objects.all()
	filter_backends = (IsUserQuestionsOnlyFilter, )
	permission_classes = (IsOwnerOrReadOnly, )

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class SubjectViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, 
					 mixins.CreateModelMixin, viewsets.GenericViewSet):
	serializer_class = SubjectSerializer
	queryset = Subject.objects.all()
	filter_backends = (IsUserSubjectsOnlyFilter, )
	permission_classes = (IsOwnerOrReadOnly, )

	@list_route(methods=['GET'])
	def inbox(self, request):
		self.filter_backends = (IsUserSubjectsOnlyFilter, IsUserNextActionOnly)
		return super(SubjectViewSet, self).list(request)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class UserViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
				  viewsets.GenericViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()
	permission_classes = (IsOwnerOrReadOnly, )