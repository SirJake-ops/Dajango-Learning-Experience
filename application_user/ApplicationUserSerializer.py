from rest_framework import serializers
from .models import ApplicationUser


class ApplicationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationUser
        fields = '__all__'


class ApplicationUserCreateUserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = ApplicationUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

    class Meta:
        model = ApplicationUser
        fields = ['email', 'username', 'password']
