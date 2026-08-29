from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from django.conf import settings


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

    def __str__(self):
        return self.user.username

    def set_medical_record(self, text):
        key = settings.FERNET_KEY.encode()
        cipher = Fernet(key)
        self.medical_record = cipher.encrypt(
            text.encode()
        ).decode()

    def get_medical_record(self):
        key = settings.FERNET_KEY.encode()
        cipher = Fernet(key)
        return cipher.decrypt(
            self.medical_record.encode()
        ).decode()


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