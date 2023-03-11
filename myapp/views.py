from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Hello world</h1>')

def hello(request, name):
    return HttpResponse('<h1>Hello %s</h1> ' % name)

def about(request):
    return HttpResponse("<h1>About</h1>")