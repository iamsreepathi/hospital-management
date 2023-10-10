from django.db import models
from patients.models import Patient
from doctors.models import Doctor
from nurses.models import Nurse


# Create your models here.
class Appointment(models.Model):
    class Status(models.IntegerChoices):
        SCHEDULED = 0
        IN_PROGRESS = 1
        COMPLETED = 2
        CANCELED = 3

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    date = models.DateField(255)
    last_visit = models.DateField()
    status = models.PositiveSmallIntegerField(
        choices=Status.choices, default=Status.SCHEDULED
    )

    class Meta:
        ordering = ["date"]
