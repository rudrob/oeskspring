from django.db import models


class Measurement(models.Model):
    time = models.FloatField()

