from django.db import models
from givestrapi.models.person import Person

class Message(models.Model):
    title = models.CharField(max_length=55)
    maker = models.CharField(max_length=55, default="")
    giver = models.ForeignKey(Person, on_delete=models.CASCADE,)
    receiver = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="message_receiver")
    number_of_players = models.IntegerField(default=1)
    skill_level = models.IntegerField(default=1)

