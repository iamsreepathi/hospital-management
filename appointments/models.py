from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from nurses.models import Nurse

GENDER = (("M", "Male"), ("F", "Female"))


# Create your models here.
class Appointment(models.Model):
    class Status(models.IntegerChoices):
        SCHEDULED = 0
        IN_PROGRESS = 1
        COMPLETED = 2
        CANCELED = 3

    full_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    address = models.CharField(255)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER, default="M")
    appt_slot = models.DateTimeField()
    reason = models.CharField(max_length=50)
    notes = models.TextField()
    status = models.PositiveSmallIntegerField(
        choices=Status.choices, default=Status.SCHEDULED
    )

    class Meta:
        ordering = ["appt_slot"]
