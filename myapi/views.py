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

class ReadingViewSet(ModelViewSet):
    queryset = SensorReading.objects.all()
    serializer_class = ReadingSerializer


    def get_queryset(self):
        """
        Implements filtering by timestamp returns readings created after the selected date  
        input as URL parameter using the YYYY-MM-DD HH:MM Format.
        Examples:
        # myapi/readings/?timestamp=2022-11-09
        # myapi/readings/?timestamp=2022-11-08T16:00:00
        """
        queryset = super(ReadingViewSet, self).get_queryset()

        timestamp = self.request.query_params.get('timestamp')
        if timestamp is not None:
            queryset = queryset.filter(timestamp__gt=timestamp)
        else:
            queryset = queryset
        return queryset