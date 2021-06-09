from django.db import models

class PersonType(models.Model):
    description = models.CharField(max_length=55)

