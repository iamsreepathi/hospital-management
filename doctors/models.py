from django.db import models
from patients.models import Patient

# Create your models here.

GENDER = (("M", "Male"), ("F", "Female"))


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER, default="M")
    specialization = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, unique=True)
    address = models.CharField(255)
    about = models.TextField()

    class Meta:
        ordering = ["first_name"]


class DoctorReview(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    text = models.TextField()
    date = models.DateField(auto_now=True)

    @property
    def unrated(self):
        return 5 - self.rating

    class Meta:
        ordering = ["rating"]
