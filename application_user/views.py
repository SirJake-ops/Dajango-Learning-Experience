from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import ApplicationUser
from .serializers import ApplicationUserCreateUserSerializer, CustomTokenObtainPairSerializer
from .serializers import ApplicationUserSerializer


class ApplicationUserListView(generics.ListAPIView):
    permission_classes = IsAuthenticated
    queryset = ApplicationUser.objects.all()
    serializer_class = ApplicationUserSerializer


class ApplicationUserCreateUserView(generics.CreateAPIView):
    queryset = ApplicationUser.objects.all()
    serializer_class = ApplicationUserCreateUserSerializer


class ApplicationUserLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
