from django.db import models


# Create your models here.
class Position(models.Model):
    company = models.CharField(max_length=25)
    title = models.CharField(max_length=25)
    location = models.CharField(max_length=25)
    time = models.CharField(max_length=25)
    description = models.TextField()
