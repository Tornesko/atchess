from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("test text for main page")


def about(request):
    return HttpResponse("test text for about page")