from django.db import models
from django.conf import global_settings
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=25)
    descripcion = models.TextField()
    code_id = models.IntegerField()

    def __str__(self):
        return self.name

class Hotel(models.Model):
    company = models.ForeignKey(Company, on_delete=True)
    name = models.CharField(max_length=130)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length  = 255)
    country = models.CharField(max_length  = 255)
    telephone_number = models.CharField(max_length=12)
    image = models.ImageField(upload_to='hotel', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(global_settings.AUTH_USER_MODEL, on_delete=False, related_name="hotel_created_by")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(global_settings.AUTH_USER_MODEL, on_delete=False, related_name="hotel_updated_by")

    def __str__(self):
        return self.name

class StatusRoom(models.Model):
    STATUS_ROOM = (
        ('DB', 'Dirty_Busy'),
        ('CB', 'Clean_Busy'),
        ('DE', 'Dirty_Empty'),
        ('CE', 'Client_Empty')
    )
    denomination = models.CharField(max_length=120, choices=STATUS_ROOM)
    description = models.TextField()

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

class TypeRoom(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="type_room/", null=True, blank=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    room_type = models.ForeignKey(TypeRoom, on_delete=False)
    capacity = models.IntegerField(default = 0)
    bedOption = models.CharField(max_length  = 255)
    price = models.FloatField()
    view = models.CharField(max_length  = 255)
    total_rooms = models.CharField(max_length  = 255)
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_status = models.ForeignKey(StatusRoom, on_delete=False, related_name="room_status")
    status = models.ManyToManyField(StatusRoom, related_name="room_statuses")

    class Meta:
        verbose_name_plural = 'Rooms'

    def __str__(self):
         return self.room_type
