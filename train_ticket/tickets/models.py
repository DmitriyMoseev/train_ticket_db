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
    travel_time = models.DurationField(
        help_text="Time needed to reach this point from the beginning "
                  "of the route")
    stop_time = models.DurationField()

    class Meta:
        db_table = 'route_point'


class Run(models.Model):
    train_name = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    route = models.ForeignKey('Route')


class Coach(models.Model):
    run = models.ForeignKey('Run')
    number = models.IntegerField(help_text="number in rake")
    coach_type = models.ForeignKey('CoachType')


class CoachType(models.Model):
    code = models.CharField(max_length=100)
    berth_number = models.IntegerField()


class Ticket(models.Model):
    coach = models.ForeignKey('Coach')
    start_point = models.ForeignKey('RoutePoint', related_name='+')
    end_point = models.ForeignKey('RoutePoint', related_name='+')
    price = models.DecimalField(max_digits=11, decimal_places=2)
    cancelled = models.BooleanField(default=False)
