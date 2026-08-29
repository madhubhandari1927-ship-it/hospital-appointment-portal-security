from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from appointments import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        'doctors/',
        views.doctor_list,
        name='doctor_list'
    ),

    path(
        'patient/<int:patient_id>/medical-record/',
        views.patient_medical_record,
        name='patient_medical_record'
    ),

    path(
        'appointment/<int:appointment_id>/',
        views.appointment_detail,
        name='appointment_detail'
    ),

    path(
        'accounts/login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html'
        ),
        name='login'
    ),
]