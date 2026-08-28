from django.urls import path
from src.pages.views import homePageView, addPageView, erasePageView

urlpatterns = [
    path('', homePageView),
    path('add', addPageView),
    path('erase', erasePageView),
]