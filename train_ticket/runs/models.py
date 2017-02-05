from __future__ import unicode_literals

from django.db import models


class Run(models.Model):

    train_name = models.CharField(max_length=100)
    route = models.ForeignKey('routes.Route')

    class Meta:
        db_table = 'run'


class Coach(models.Model):

    run = models.ForeignKey('Run')
    number = models.IntegerField(help_text="number in rake")
    coach_type = models.ForeignKey('CoachType')

    class Meta:
        db_table = 'coach'


class CoachType(models.Model):

    code = models.CharField(max_length=100)
    number_of_berths = models.PositiveIntegerField()

    class Meta:
        db_table = 'coach_type'
