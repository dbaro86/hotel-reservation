from django.shortcuts import render
from rest_framework import viewsets
from .models import StatusReservation
from .serializers import StatusReservationSerializer

# Create your views here.



class StatusReservationViewSets(viewsets.ModelViewSet):
    queryset = StatusReservation.objects.all()
    serializer_class = StatusReservationSerializer