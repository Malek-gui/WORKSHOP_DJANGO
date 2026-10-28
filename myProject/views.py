
from django.http import HttpResponse


def homePage(request):
    return HttpResponse("Welcome to home page")


def homePageName(request, name):
    return HttpResponse(f"Welcome to home page {name}")
