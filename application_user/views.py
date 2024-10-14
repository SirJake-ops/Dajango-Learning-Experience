from django.http import HttpResponse
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import ApplicationUser
from .serializers import ApplicationUserCreateUserSerializer, CustomTokenObtainPairSerializer
from .serializers import ApplicationUserSerializer


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


class ApplicationUserLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    pass
