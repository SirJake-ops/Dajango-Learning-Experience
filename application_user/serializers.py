import logging

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import ApplicationUser

logger = logging.getLogger(__name__)


class ApplicationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationUser
        fields = '__all__'


class ApplicationUserCreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = ApplicationUser(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
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

        try:
            user = ApplicationUser.objects.get(email=email)
        except ApplicationUser.DoesNotExist:
            logger.debug(f"user is not valid: {email}, {password}")
            raise serializers.ValidationError('Invalid username or password')

        if not check_password(password, user.password):
            logger.debug(f"password does not match for user: {email}")
            raise serializers.ValidationError('Invalid username or password')

        refresh = self.get_token(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.id,
        }
