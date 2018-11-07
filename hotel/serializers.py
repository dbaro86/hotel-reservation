from rest_framework import serializers
from .models import Company, Hotel, StatusRoom, TypeRoom, Room


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class StatusRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusRoom
        fields = '__all__'





class TypeRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeRoom
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'



