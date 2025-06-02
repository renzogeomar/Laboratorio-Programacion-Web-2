from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse

# Create your views here.
def home(request):
    return HTTPResponse("Hello, Telusko!")