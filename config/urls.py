from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from portal import views


urlpatterns = [

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path(
        'appointment/<int:appointment_id>/',
        views.appointment_detail,
        name='appointment_detail'
    ),

    path(
        'patient/<int:patient_id>/',
        views.public_patient_information,
        name='patient_information'
    ),

    path(
        'review/',
        views.add_review,
        name='add_review'
    ),
]