from django.http import HttpResponse
from rest_framework import generics

from .TrackerSerializer import TrackerCreateSerializer, TrackerSerializer, TrackerDeleteSerializer
from .models import Bug


class BugTrackerListView(generics.ListCreateAPIView):
    queryset = Bug.objects.all()
    serializer_class = TrackerSerializer


class BugTrackerCreateView(generics.CreateAPIView):
    queryset = Bug.objects.all()
    serializer_class = TrackerCreateSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            return HttpResponse("Bug created successfully")
        return response


class BugTrackerDeleteView(generics.DestroyAPIView):
    queryset = Bug.objects.all()
    serializer_class = TrackerDeleteSerializer

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        if response.status_code == 204:
            return HttpResponse("Bug deleted successfully")
        return response
