from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApplicationUserListCreateView.as_view(), name='user-list-create'),
    path('create', views.ApplicationUserCreateUserView.as_view(), name='user-create'),
    path('login', views.ApplicationUserLoginView.as_view(), name='user-login'),
]
