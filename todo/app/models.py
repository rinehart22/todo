from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Person(models.Model):
    name =models.CharField(max_length=100)
    age= models.PositiveBigIntegerField()

    def __str__(self):
        return self.name 