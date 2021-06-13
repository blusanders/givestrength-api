from django.db import models

class Day(models.Model):
    day = models.CharField(max_length=55)

    def __str__(self):
        return self.day