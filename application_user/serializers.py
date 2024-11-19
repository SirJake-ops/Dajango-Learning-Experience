from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

from .models import ApplicationUser


class ApplicationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationUser
        fields = '__all__'


class ApplicationUserCreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = ApplicationUser(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        user.set_password(validated_data['password'])  # This right here is already hashed quit asking to hash it again
        user.save()
        return user

    class Meta:
        model = ApplicationUser
        fields = ['email', 'username', 'password']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        request = self.context.get('request')
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(username=email, password=password, request=request)
        if user is None:
            raise serializers.ValidationError('Invalid username or password')

        refresh = self.get_token(user)

        return {
            'refresh': str(refresh),
        }
