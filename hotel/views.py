from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *

from .models import *
# Create your views here.


class HotelViewSets(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
