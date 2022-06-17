from django.db import models

# Create your models here.
class Bus(models.Model):
    bus_no=models.CharField(max_length=100)
    bus_manufacturer=models.CharField(max_length=100)

class Trip(models.Model):
    bus=models.ForeignKey(Bus, related_name='bus_id', on_delete=models.CASCADE)
    source=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    no_of_seats=models.IntegerField()
    no_of_seats_left=models.IntegerField()

    def __str__(self):
        return self.source


class Bookings(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    
    
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)

    def __str__(self):
        return self.email
