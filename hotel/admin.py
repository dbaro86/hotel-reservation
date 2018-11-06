from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code_id')


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'address', 'created_at', 'updated_at')


admin.site.register(StatusRoom)
admin.site.register(StatusReservation)
admin.site.register(TypeRoom)
admin.site.register(Room)
