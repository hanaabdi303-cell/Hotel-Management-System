from django.db import models

class RoomCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Occupied', 'Occupied'),
        ('Maintenance', 'Maintenance'),
    ]
    room_number = models.CharField(max_length=10, unique=True)
    category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')

    def __str__(self):
        return f"Room {self.room_number} ({self.category.name})"

class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=200, default='Hargeisa')
    id_number = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name


class Reservation(models.Model):
    STATUS_CHOICES = [
        ('Booked', 'Booked'),
        ('Checked-In', 'Checked-In'),
        ('Checked-Out', 'Checked-Out'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Booked')

    def __str__(self):
        return f"{self.customer.full_name} - Room {self.room.room_number}"