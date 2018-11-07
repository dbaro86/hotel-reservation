from rest_framework import serializers
from .models import StatusReservation

class StatusReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusReservation
        fields = '__all__'