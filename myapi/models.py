from django.db import models
from django.urls import reverse

# Create your models here.

class Sensor(models.Model):
    # Sensor types
    SENSOR_TYPES = [
    # (value_in_db, display)
    ('Humidity', 'Humidity'),
    ('Temperature', 'Temperature'),
    ('Acoustic', 'Acoustic'),
    ]
    # Fields
    type = models.CharField(choices=SENSOR_TYPES, max_length=12)
    vendor_name = models.CharField(max_length=120)
    vendor_email = models.EmailField()
    description = models.TextField()
    location = models.CharField(max_length=3) # TODO: change into point

    # Metadata
    class Meta: 
        # default ordering of records returned when model type is queried
        ordering = ['id'] # 'field' (ascending) or '-field' (descending)

    def __str__(self) -> str:
        """return a human-readable string for each Sensor object (appears in Admin site etc.)"""
        return self.vendor_name+" Sensor:"+self.id+" - Location: "+self.location


    

class SensorReading(models.Model):
    pass