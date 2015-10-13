from rest_framework import serializers
from users.models import User

# class UserSerializer(serializers.Serializer):
# 	pk = serializers.IntegerField(read_only=True)
# 	name = serializers.CharField(required=True, max_length=50)
# 	email = serializers.CharField(required=True, max_length=100)
# 	password = serializers.CharField(required=True, max_length=30)

# 	def create(self, validated_data):
# 		"""
# 		Create and return a new 'User' instance
# 		"""
# 		return User.objects.create(**validated_data)

# 	def update(self, instance, validated_data):
# 		"""
# 		Update and return an existing 'User' instance
# 		"""
# 		instance.name = validated_data.get('name', instance.name)
# 		instance.email = validated_data.get('email', instance.email)
# 		instance.password = validated_data.get('password', instance.password)
# 		instance.save()
# 		return instance

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'name', 'email', 'password', 'created')