from django.db import models
from givestrapi.models.person import Person
from django.utils import timezone

class Message(models.Model):
    body = models.CharField(max_length=55)
    giver = models.ForeignKey(Person, on_delete=models.CASCADE,)
    receiver = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="message_receiver")
    created = models.DateTimeField(default=timezone.now)
