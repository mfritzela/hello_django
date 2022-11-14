# Hello Django

This is a test project for the implementation of a REST API using Django REST framework.

## Problem statement

Development of a simple REST API which will be a reporting service for an IoT platform.
There are three types of sensors that can generate readings:
- Humidity Sensor
- Temperature Sensor
- Acoustic Sensor

The API should be allow the following operations:
1. Store information about each sensor
2. Store a sensor reading (belonging to a specific sensor). 
3. Query the readings 

The responses should be returned paginated with a page size 10.

## Data Models

Django models are the Python classes that represent the objects in the database.

