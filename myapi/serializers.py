from rest_framework import serializers
from .models import Sensor, SensorReading

class SensorSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Sensor
        fields = ('id', 'type', 'vendor_name', 'vendor_email', 'description', 'location')
        
class ReadingSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        model = SensorReading
        fields = ('id', 'sensorId', 'reading', 'description', 'timestamp')