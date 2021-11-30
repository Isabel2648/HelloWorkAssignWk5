from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World! Isabel Flores is here!")
