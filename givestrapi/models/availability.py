from django.db import models
from django.contrib.auth.models import User

class Availability(models.Model):
    person = models.ForeignKey("Person", on_delete=models.CASCADE,)
    day = models.IntegerField(default=0)
    time_start = models.TimeField()
    time_end = models.TimeField()
    on_call = models.IntegerField(default=0)

