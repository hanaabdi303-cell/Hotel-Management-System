from django.contrib import admin
from .models import RoomCategory, Room, Customer, Reservation

admin.site.register(RoomCategory)
admin.site.register(Room)
admin.site.register(Customer)
admin.site.register(Reservation)