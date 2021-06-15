from django.db import models

class Gender(models.Model):
    description = models.CharField(max_length=2)

