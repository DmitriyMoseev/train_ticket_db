from __future__ import unicode_literals

from django.db import models


class Ticket(models.Model):

    coach = models.ForeignKey('runs.Coach')
    berth_number = models.PositiveIntegerField(null=True)
    start_station = models.ForeignKey('routes.Station', related_name='+')
    end_station = models.ForeignKey('routes.Station', related_name='+')
    price = models.DecimalField(max_digits=11, decimal_places=2)
    cancelled = models.BooleanField(default=False)
    passenger = models.ForeignKey('Passenger')

    class Meta:
        db_table = 'ticket'


class Passenger(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_number = models.CharField(max_length=20)

    class Meta:
        db_table = 'passenger'
