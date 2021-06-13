from django.db import models

class HelpType(models.Model):
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=55)

    def __str__(self):
        return self.name