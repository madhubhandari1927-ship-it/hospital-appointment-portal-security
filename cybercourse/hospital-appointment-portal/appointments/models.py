from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet


FERNET_KEY = b"gwRCnI8cqSedX-xOYB_XUthg67vABleo3s4EmxqY6Co="
cipher = Fernet(FERNET_KEY)


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PatientProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    phone = models.CharField(max_length=20)

    medical_record = models.TextField()

    def set_medical_record(self, value):
        self.medical_record = cipher.encrypt(
            value.encode()
        ).decode()

    def get_medical_record(self):
        return cipher.decrypt(
            self.medical_record.encode()
        ).decode()

    def __str__(self):
        return self.user.username


class Appointment(models.Model):
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='appointments'
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    appointment_date = models.DateTimeField()

    reason = models.TextField()

    def __str__(self):
        return (
            f"{self.patient.username} - "
            f"{self.doctor.name}"
        )