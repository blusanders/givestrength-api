from django.db import models
from givestr.models.person import Person


class Message(models.Model):
    title = models.CharField(max_length=55)
    maker = models.CharField(max_length=55, default="")
    giver = models.ForeignKey(Person, on_delete=models.CASCADE, default=0)
    receiver = models.ForeignKey(Person, on_delete=models.CASCADE,)
    number_of_players = models.IntegerField(default=1)
    skill_level = models.IntegerField(default=1)
