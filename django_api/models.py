from django.db import models


class Drink(models.Model):
    DoesNotExist = None
    objects = None
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
