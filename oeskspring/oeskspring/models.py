from django.db import models


class Measurement(models.Model):
    done = models.BooleanField()
    avg = models.FloatField()
    median = models.FloatField()
    iqr = models.FloatField()
    stdev = models.FloatField()

