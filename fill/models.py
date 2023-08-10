from django.db import models

# Create your models here.


class Details(models.Model):
    full_name = models.CharField(max_length=200)
    location = models.CharField(max_length=1000)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)