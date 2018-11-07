from django.contrib import admin
from .models import StatusReservation
# Register your models here.


@admin.register(StatusReservation)
class StatusReservationAdmin(admin.ModelAdmin):
    list_display = ['denomination', 'description']