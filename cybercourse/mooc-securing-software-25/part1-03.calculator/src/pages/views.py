from django.http import HttpResponse


def add(request):
    first = int(request.GET["first"])
    second = int(request.GET["second"])
    return HttpResponse(first + second)


def multiply(request):
    first = int(request.GET["first"])
    second = int(request.GET["second"])
    return HttpResponse(first * second)