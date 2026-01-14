from django.db import models

# Create your models here.


class Resident(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    age = models.IntegerField()
    nationality = models.CharField(max_length=250)
