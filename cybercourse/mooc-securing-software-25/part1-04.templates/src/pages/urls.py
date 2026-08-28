from django.urls import path
from .views import homePageView, videoPageView

urlpatterns = [
    path("", homePageView),
    path("video/", videoPageView),]