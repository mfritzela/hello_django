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
        return " ID:"+str(self.id)+" | "+self.vendor_name+" Sensor - Location: "+self.location


class SensorReading(models.Model):
    # Fields
    sensorId = models.ForeignKey(Sensor, on_delete=models.CASCADE) 
    # If the user deletes a sensor, the sensor readings belonging to that sensoor will be deleted
    reading = models.JSONField() # {'type': 'int', 'value': 5}
    description = models.TextField()
    timestamp = models.DateTimeField() # date and time the reading was sent

    # Metadata
    class Meta:
        # default ordering of records returned when model type is queried
        ordering = ['-timestamp']

    def __str__(self) -> str:
        """return a human-readable string for each Sensor object (appears in Admin site etc.)"""
        return "Reading: "+str(self.id)+" Sensor:"+str(self.sensorId)+" - Timestamp: "+str(self.timestamp)