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

# class Bookings(models.model):