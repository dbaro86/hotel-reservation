from django.db import models
from django.conf import global_settings

from hotel.models import Hotel, TypeRoom

# Create your models here.
class Guest(models.Model):
    name = models.ForeignKey(global_settings.AUTH_USER_MODEL, on_delete=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)

class StatusReservation(models.Model):
    STATUS_ROOM = (
        ('R', 'RESERVED'),
        ('RQ', 'REQUESTED'),
        ('A', 'AVAILABLE'),
        ('P', 'PROGRESS')
    )
    denomination = models.CharField(max_length=120, choices=STATUS_ROOM)
    description = models.TextField()

    def __str__(self):
        return self.denomination

class Requirements(models.Model):
    denomination = models.CharField(max_length=100)
    description = models.TextField()


class TypeRoomCant(models.Model):
    type_room = models.ForeignKey(TypeRoom, on_delete=True)
    cant = models.IntegerField()
    requirements = models.ManyToManyField(Requirements)


class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=True)
    hotel = models.ForeignKey(Hotel, on_delete=True)
    type_room = models.ForeignKey(TypeRoomCant, on_delete=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(global_settings.AUTH_USER_MODEL, on_delete=False, related_name="request_reservation_created_by")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(global_settings.AUTH_USER_MODEL, on_delete=False, related_name="request_reservation_updated_by")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    requirements = models.ManyToManyField(Requirements)
    last_status = models.ForeignKey(StatusReservation, on_delete=False, related_name="reservation_status")
    status = models.ManyToManyField(StatusReservation, related_name="reservation_statuses")

    class Meta:
        verbose_name_plural = 'Requests Reservation'


