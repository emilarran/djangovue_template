from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from snippr.models.userprofile import UserProfile
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = (
			'username', 'first_name', 'last_name', 'email', 'password')

	def create(self, validated_data):
		user = User.objects.create_user(**validated_data)
		user.save()
		UserProfile.objects.create(user=user)
		Token.objects.create(user=user)
		return user


class LoginSerializer(serializers.HyperlinkedModelSerializer):
	token = serializers.SerializerMethodField()

	class Meta:
		model = User
		fields = (
			'pk', 'username', 'first_name', 'last_name', 'email', 'token')

	def get_token(self, obj):
		ret = Token.objects.filter(user=obj).all().values('key')
		return ret