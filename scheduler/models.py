from django.db import models

# Create your models here.

class Truck(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

class Driver(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    current_status = models.CharField(max_length=50)
    status_start_time = models.DateTimeField()
