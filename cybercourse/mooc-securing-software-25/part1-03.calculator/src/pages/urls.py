from django.urls import path
from .views import add, multiply

urlpatterns = [
    path("add/", add),
    path("multiply/", multiply),
]