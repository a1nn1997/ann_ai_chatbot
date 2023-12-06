from django.contrib.auth.models import User
from user.models import Profile
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class PasswordChangeSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
