from __future__ import unicode_literals

from django.db import models


class Station(models.Model):

    name = models.CharField(max_length=100)
    area = models.CharField(
        max_length=100,
        help_text="City or village name or anything describing location")

    class Meta:
        db_table = 'station'


class Route(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'route'


class RoutePoint(models.Model):

    route = models.ForeignKey('Route')
    station = models.ForeignKey('Station')
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()

    class Meta:
        db_table = 'route_point'


