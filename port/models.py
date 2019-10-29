from django.db import models
import datetime

from django.db import models
from django.utils import timezone


class Condition(models.Model):
    code = models.CharField(max_length=50, null=True)
    start_date = models.CharField(max_length=50, null=True)
    end_date = models.CharField(max_length=50, null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.code

class Jongmok(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)

    def __str__(self):  # __unicode__ on Python 2
        return self.name
