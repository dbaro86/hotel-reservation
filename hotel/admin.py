from django.contrib import admin

from .models import Company, Hotel, StatusRoom, TypeRoom, Room
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code_id')


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'address', 'created_at', 'updated_at')



@admin.register(StatusRoom)
class StatusRoomAdmin(admin.ModelAdmin):
    list_display = ['denomination', 'description']


@admin.register(TypeRoom)
class TypeRoomAdmin(admin.ModelAdmin):
    list_display = ['room_type', 'description']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'room_type', ]
