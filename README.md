# Hello Django

This is a test project for the implementation of a REST API using Django REST framework.

## Problem statement

Development of a simple REST API which will be a reporting service for an IoT platform.
There are three types of sensors that can generate readings:
- Humidity Sensor
- Temperature Sensor
- Acoustic Sensor

The API should allow the following operations:
1. Store information about each sensor
2. Store a sensor reading (belonging to a specific sensor). 
3. Query the readings 

The responses should be returned paginated with a page size 10.

## Data Models

Django models are the Python classes that represent the objects in the database.

![image](https://user-images.githubusercontent.com/113194115/201877974-217c4487-5b30-46bd-b27a-0c7835f2a914.png)

There are two models, for the **Sensors** and the **Sensor Readings**. They are linked by a foreign key, the SensorReading references the Sensor's primary key, defining a one-to-many relationship: A sensor can have more than one readings belonging to it, but each Sensor Reading belongs to a single Sensor. 
On a delete operation the behavior is set to CASCADE, meaning that if a sensor instance is deleted, all of its associated readings are deleted from the database.

### Sensor Model
The field `type` of the `Sensor` model is restricted to allow only valid sensor types (Humidity, Temperature, Acoustic).

### SensorReading Model
The field `reading` of the `SensorReading` model is defined to be a JSON field, to allow flexibilty for different types of reading data and possible extensions. `SensorReading` instances are expected to have a "type" and a "value" property (e.g. `{"type": "int", "value": 5}`) at minimum. <br> *It is assumed that each type of Sensor produces one type of reading only.*

## API Reference

### Sensors

| **Endpoint**                          | **GET**                                              | **POST**                   | **PUT/PATCH**                             | **DELETE**                 |
|---------------------------------------|------------------------------------------------------|----------------------------|-------------------------------------------|----------------------------|
| /sensors                              | Show collection of sensors                           | Create new sensor instance |                                           |                            |
| /sensors/{id}                         | Show information of sensor with id={id}              |                            | Update information of sensor with id={id} | Delete sensor with id={id} |
| /sensors/{id}/readings                | Show readings of sensor with id={id}                 |                            |                                           |                            |
| /sensors/type/{type}                  | Show collection of sensors of type={type}            |                            |                                           |                            |
| /sensors/type/{type}/readings         | Show readings of sensors of type={type}              |                            |                                           |                            |
| /sensors/location/{location}          | Show collection of sensors where location={location} |                            |                                           |                            |
| /sensors/location/{location}/readings | Show readings of sensors where location={location}   |                            |                                           |                            |
| /sensors/{id}/readings/stats          | Show statistics of readings of sensor with id={id}   |                            |                                           |                            |

### Sensor Readings

| **Endpoint**                                 | **GET**                                                       | **POST**                             | **PUT/PATCH**               | **DELETE**                 |
|----------------------------------------------|---------------------------------------------------------------|--------------------------------------|-----------------------------|----------------------------|
| /readings                                    | Show collection of readings                                   | Create a new sensor reading instance |                             |                            |
| /readings/{id}                               | Show reading with id={id}                                     |                                      | Update reading with id={id} | Delete sensor with id={id} |
| /readings/?timestamp={YYYY-MM-DDTHH:MM}      | Show readings created at the specified datetime               |                                      |                             |                            |
| /readings/?from_timestamp={YYYY-MM-DDTHH:MM} | Show readings created after the specified datetime            |                                      |                             |                            |
| /readings/?ordering={ordering_field}         | Show readings ordered by one of the specified ordering fields |                                      |                             |                            |

Notes:
1. URL parameters can be conbined to create more complex queries. 
2. For the timestamp URL parameter, hours and minutes can be ommited (defaults to 00:00).
3. Ordering is asceding, but can be descending by prepending a `-` to the odering field.

Example: `/readings/?from_timestamp=2022-11-08&ordering=-reading__value`

#### Ordering Fields

* reading__value
* timestamp
