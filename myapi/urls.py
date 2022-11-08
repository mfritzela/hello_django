from django.contrib import admin
from django.urls import path
from . import views
from rest_framework import routers


# the name parameter is a unique identifier for a url mapping
# the name can be used to 'reverse' the mapper
urlpatterns = [

]

router = routers.DefaultRouter()
router.register(r'sensors', views.SensorViewSet)
router.register(r'readings', views.ReadingViewSet)

urlpatterns += router.urls