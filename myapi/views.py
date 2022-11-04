from django.shortcuts import render

from .models import Sensor
from .serializers import SensorSerializer
from rest_framework import viewsets

# Create your views here.


class SensorViewSet(viewsets.ModelViewSet):
    """
    Includes implementations for the following actions: list, create, update, partial_update, destroy
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer