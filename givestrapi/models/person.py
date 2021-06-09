from givestrapi.models.person_type import PersonType
from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    person_type = models.ForeignKey(PersonType, on_delete=models.CASCADE,)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)
    phone = models.CharField(max_length=10)
    bio = models.CharField(max_length=255)
    popup = models.CharField(max_length=100)
    latitude = models.IntegerField(default=0)
    longitude = models.IntegerField(default=0)
