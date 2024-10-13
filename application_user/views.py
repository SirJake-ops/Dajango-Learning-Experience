from django.http import HttpResponse
from rest_framework import generics

from .ApplicationUserSerializer import ApplicationUserCreateUserSerializer
from .models import ApplicationUser
from .ApplicationUserSerializer import ApplicationUserSerializer


class ApplicationUserListCreateView(generics.ListCreateAPIView):
    queryset = ApplicationUser.objects.all()
    serializer_class = ApplicationUserSerializer


class ApplicationUserCreateUserView(generics.CreateAPIView):
    queryset = ApplicationUser.objects.all()
    serializer_class = ApplicationUserCreateUserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            return HttpResponse("User created successfully")
        return response


class ApplicationUserLoginView(generics.CreateAPIView):
    queryset = ApplicationUser.objects.all()
    serializer_class = ApplicationUserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            return HttpResponse("User logged in successfully")
        return response

    def token(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            return HttpResponse("Token created successfully")
        return response
