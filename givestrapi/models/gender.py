from django.db import models

class Gender(models.Model):
    name = models.CharField(max_length=2)
    description = models.CharField(max_length=2)
    

