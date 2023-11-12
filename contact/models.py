from django.db import models


# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    message = models.TextField()


