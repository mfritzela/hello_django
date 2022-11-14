from argparse import Action
from django.shortcuts import render

from .models import Sensor, SensorReading
from .serializers import SensorSerializer, ReadingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class SensorViewSet(ModelViewSet):
    """
    Includes implementations for the following actions: list, create, update, partial_update, destroy
    Filter sensors by type: /sensors/type/{type}
    Filter sensors by location: /sensors/location/{location}
    Show readings of a specific sensor: /sensors/{id}/readings
    Show readings of a specific type of sensor: /sensors/type/{type}/readings
    Show readings of sensor of specific location: /sensors/location/{location}/readings
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    # sensors/type/{type_name} GET sensors of type = {type_name}
    @action(detail=False, url_path=r'type/(?P<type_name>\w+)', url_name='type')
    def sensor_type(self, request, type_name):
        # check sensor type validity
        if (type_name, type_name) not in Sensor.SENSOR_TYPES:
            return Response({'detail': 'Invalid Sensor Type.'}, status=400)
        query = Sensor.objects.filter(type=type_name)
        serializer = SensorSerializer(query, many=True)
        return Response(serializer.data)

    # sensors/location/{location} GET sensors of location = {location}
    @action(detail=False, url_path=r'location/(?P<location>\w+)', url_name='location')
    def sensor_location(self, request, location):
        query = Sensor.objects.filter(location=location)
        serializer = SensorSerializer(query, many=True)
        return Response(serializer.data)

    # sensors/{id}/readings GET readings of sensor id = {id}
    @action(detail=True, url_path='readings', url_name='readings')
    def sensor_readings(self, request, pk=None):
        query = SensorReading.objects.filter(sensorId=pk)
        serializer = ReadingSerializer(query, many=True)
        return Response(serializer.data)

    # sensors/type/{type}/readings GET readings of sensors of type = {type}
    @action(detail=False, url_path=r'type/(?P<type_name>\w+)/readings', url_name='readings-type')
    def sensor_readings_type(self, request, type_name):
        query = SensorReading.objects.filter(sensorId__type=type_name)
        serializer = ReadingSerializer(query, many=True)
        return Response(serializer.data)

    # sensors/location/{location}/readings GET readings of sensors of location = {location}
    @action(detail=False, url_path=r'location/(?P<location>\w+)/readings', url_name='readings-location')
    def sensor_readings_location(self, request, location):
        query = SensorReading.objects.filter(sensorId__location= location)
        serializer = ReadingSerializer(query, many=True)
        return Response(serializer.data)


class ReadingViewSet(ModelViewSet):
    queryset = SensorReading.objects.all()
    serializer_class = ReadingSerializer
    
    def get_queryset(self):
        """
        Implements filtering by the following URL parameters:
        - from_timestamp returns readings created after the selected datetime
        - timestamp returns readings created at the specific datetime
        input as  using the YYYY-MM-DD HH:MM Format. (time can be ommited)
        Examples:
        # myapi/readings/?timestamp=2022-11-09
        # myapi/readings/?timestamp=2022-11-08T16:00:00
        """
        queryset = super(ReadingViewSet, self).get_queryset()

        timestamp = self.request.query_params.get('timestamp')
        from_timestamp = self.request.query_params.get('from_timestamp')
        if from_timestamp is not None:
            queryset = queryset.filter(timestamp__gt=from_timestamp)
        elif timestamp is not None:
            queryset = queryset.filter(timestamp=timestamp)
        else:
            queryset = queryset
        return queryset