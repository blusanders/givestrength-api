from django.db import models

class PersonType(models.Model):
    description = models.CharField(max_length=55)

    def __str__(self):
        return self.description