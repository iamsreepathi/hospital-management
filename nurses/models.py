from django.db import models


# Create your models here.
class Nurse(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)

    class Meta:
        ordering = ["first_name"]
