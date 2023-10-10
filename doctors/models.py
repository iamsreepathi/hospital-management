from django.db import models

# Create your models here.


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    address = models.CharField(255)
    about = models.TextField()

    class Meta:
        ordering = ["first_name"]
