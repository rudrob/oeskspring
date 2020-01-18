from django.db import models


class Measurement(models.Model):
    jarname = models.TextField(max_length=100, blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    times = models.IntegerField(default=1)
    done = models.BooleanField(default=False)
    failed = models.BooleanField(default=False)
    avg = models.FloatField(blank=True, null=True)
    median = models.FloatField(blank=True, null=True)
    iqr = models.FloatField(blank=True, null=True)
    stdev = models.FloatField(blank=True, null=True)
    namespace = models.TextField(max_length=50, blank=True, null=True)

