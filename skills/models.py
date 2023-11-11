from django.db import models

# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length=25)


class Langauges(models.Model):
    name = models.CharField(max_length=25)
