from django.db import models


class Measurement(models.Model):
    jarname = models.TextField(max_length=100)
    enddate = models.DateTimeField()
    times = models.IntegerField()
    done = models.BooleanField(default=False)
    failed = models.BooleanField(default=False)
    avg = models.FloatField()
    median = models.FloatField()
    iqr = models.FloatField()
    stdev = models.FloatField()
    namespace = models.TextField(max_length=50)

