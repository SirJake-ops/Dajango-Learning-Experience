from django.urls import path

from . import views

urlpatterns = [
    path('', views.BugTrackerListView.as_view(), name='bug-list-create'),
    path('create/', views.BugTrackerCreateView.as_view(), name='bug-create'),
]
