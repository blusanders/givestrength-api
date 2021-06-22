from givestrapi.models.person_type import PersonType
from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    person_type = models.ForeignKey("PersonType", on_delete=models.CASCADE,)
    street = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=2, default="")
    zip = models.CharField(max_length=5, default="")
    phone = models.CharField(max_length=10, default="")
    bio = models.TextField(max_length=255, default="")
    popup = models.CharField(max_length=100, default="")
    latitude = models.FloatField(default=0 )
    longitude = models.FloatField(default=0)
    on_call = models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name_plural = "Person"
        ordering = ['user']

    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, value):
            self.__distance = value
    
    