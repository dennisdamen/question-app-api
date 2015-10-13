from django.shortcuts import render

###################################################
# TUT1
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from users.models import User
# from users.serializers import UserSerializer

###################################################
# TUT2
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from users.models import User
# from users.serializers import UserSerializer

###################################################
# TUT3.1
# from users.models import User
# from users.serializers import UserSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

###################################################
# TUT3.2 mixins
# from users.models import User
# from users.serializers import UserSerializer
# from rest_framework import mixins
# from rest_framework import generics

###################################################
# TUT3.3 generic class based views
from users.models import User
from users.serializers import UserSerializer
from rest_framework import generics

###################################################
# TUT1
# class JSONResponse(HttpResponse):
# 	"""
# 	An HttpResponse that renders its content into JSONParser
# 	"""
# 	def __init__(self, data, **kwargs):
# 		content = JSONRenderer().render(data)
# 		kwargs['content_type'] = 'application/json'
# 		super(JSONResponse, self).__init__(content, **kwargs)

# @csrf_exempt
# def users_list(request):
# 	"""
# 	List all the users or create a new users
# 	"""
# 	if request.method == 'GET':
# 		users = User.objects.all()
# 		serializer = UserSerializer(users, many=True)
# 		return JSONResponse(serializer.data)

# 	elif request.method == 'POST':
# 		data = JSONParser().parse(request)
# 		serializer = UserSerializer(data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JSONResponse(serializer.data, status=201)
# 		return JSONResponse(serializer.errors, status=400)

###################################################
# TUT2
# @api_view(['GET', 'PUT'])
# def users_list(request, format=None):
# 	"""
# 	List all the users or create a new users
# 	"""
# 	if request.method == 'GET':
# 		users = User.objects.all()
# 		serializer = UserSerializer(users, many=True)
# 		return Response(serializer.data)

# 	elif request.method == 'PUT':
# 		# data = JSONParser().parse(request)
# 		serializer = UserSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

###################################################
# TUT3.1
# class UserList(APIView):
# 	"""
# 	List all the users or create a new users
# 	"""
# 	def get(self, request, format=None):
# 		users = User.objects.all()
# 		serializer = UserSerializer(users, many=True)
# 		return Response(serializer.data)

# 	def post(self, request, format=None):
# 		serializer = UserSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

###################################################
# TUT3.2 mixins
# class UserList(	mixins.ListModelMixin,
# 				mixins.CreateModelMixin,
# 				generics.GenericAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer

# 	def get(self, request, *args, **kwargs):
# 		return self.list(request, *args, **kwargs)

# 	def post(self, request, *args, **kwargs):
# 		return self.create(request, *args, **kwargs)

###################################################
# TUT3.2 generic class based views

class UserList(	generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

###################################################
# TUT1
# @csrf_exempt
# def user_detail(request, pk):
# 	"""
# 	Retrieve, update or delete a users
# 	"""
# 	try:
# 		user = User.objects.get(pk=pk)
# 	except User.DoesNotExist:
# 		return HttpResponse(status=404)

# 	if request.method == 'GET':
# 		serializer = UserSerializer(user)
# 		return JSONResponse(serializer.data)

# 	elif request.method == 'PUT':
# 		data = JSONParser().parse(request)
# 		serializer = UserSerializer(user, data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JSONResponse(serializer.data)
# 		return JSONResponse(serializer.errors, status=400)

# 	elif request.method == 'DELETE':
# 		user.delete()
# 		return HttpResponse(status=204)

###################################################
# TUT2
# @api_view(['GET', 'PUT', 'DELETE'])
# def user_detail(request, pk, format=None):
# 	"""
# 	Retrieve, update or delete a users
# 	"""
# 	try:
# 		user = User.objects.get(pk=pk)
# 	except User.DoesNotExist:
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'GET':
# 		serializer = UserSerializer(user)
# 		return Response(serializer.data)

# 	elif request.method == 'PUT':
# 		serializer = UserSerializer(user, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	elif request.method == 'DELETE':
# 		user.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)

###################################################
# TUT3.1
# class UserDetail(APIView):
# 	"""
# 	Retrieve, update or delete a users
# 	"""
# 	def get_object(self, pk):
# 		try:
# 			return User.objects.get(pk=pk)
# 		except User.DoesNotExist:
# 			raise Http404

# 	def get(self, request, pk, format=None):
# 		user = self.get_object(pk)
# 		serializer = UserSerializer(user)
# 		return Response(serializer.data)

# 	def put(self, request, pk, format=None):
# 		user = self.get_object(pk)
# 		serializer = UserSerializer(user, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	def delete(self, request, pk, format=None):
# 		user = self.get_object(pk)
# 		user.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)

###################################################
# TUT3.2 mixins
# class UserDetail(	mixins.RetrieveModelMixin,
# 					mixins.UpdateModelMixin,
# 					mixins.DestroyModelMixin,
# 					generics.GenericAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer

# 	def get(self, request, *args, **kwargs):
# 		return self.retrieve(request, *args, **kwargs)

# 	def put(self, request, *args, **kwargs):
# 		return self.update(request, *args, **kwargs)

# 	def delete(self, request, *args, **kwargs):
# 		return self.destroy(request, *args, **kwargs)