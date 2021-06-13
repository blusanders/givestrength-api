from django.db import models
from django.contrib.auth.models import User

class Availability(models.Model):
    person = models.ForeignKey("Person", on_delete=models.CASCADE,)
    day = models.ForeignKey("Day", on_delete=models.CASCADE,)
    time_start = models.TimeField(null=True, blank=True)
    time_end = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.person.user.first_name + " - " + self.day.day

    class Meta:
        verbose_name_plural = "Availability"
        ordering = ['person']