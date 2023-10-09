from django.db import models


# Create your models here.
class Patient(models.Model):
    GENDER = (("M", "Male"), ("F", "Female"))

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER, default="M")
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=255)
    insurance_info = models.CharField(max_length=20)

    class Meta:
        ordering = ["first_name"]
