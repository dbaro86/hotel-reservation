from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CompanySerializer, HotelSerializer, StatusRoomSerializer, \
    TypeRoomSerializer, RoomSerializer

from .models import Company, Hotel, StatusRoom, TypeRoom, Room

# Create your views here.


class CompanyViewSets(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class HotelViewSets(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class StatusRoomViewSets(viewsets.ModelViewSet):
    queryset = StatusRoom.objects.all()
    serializer_class = StatusRoomSerializer




class TypeRoomViewSets(viewsets.ModelViewSet):
    queryset = TypeRoom.objects.all()
    serializer_class = TypeRoomSerializer


class RoomViewSets(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer