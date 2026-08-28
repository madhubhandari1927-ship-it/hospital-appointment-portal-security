from django.shortcuts import render


def homePageView(request):
    return render(request, "pages/index.html")


def videoPageView(request):
    return render(request, "pages/video.html")