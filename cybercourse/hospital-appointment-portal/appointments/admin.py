from django.contrib import admin
from .models import Doctor, PatientProfile, Appointment

admin.site.register(Doctor)
admin.site.register(PatientProfile)
admin.site.register(Appointment)