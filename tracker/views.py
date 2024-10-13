from django.http import HttpResponse
from rest_framework import generics
from .TrackerSerializer import TrackerCreateSerializer, TrackerSerializer
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
