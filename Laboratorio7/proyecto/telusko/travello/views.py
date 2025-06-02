from django.shortcuts import render
from .models import DestinosTuristicos

# Create your views here.
def index(request):
    return render(request, 'index.html')
def destinos(request):
    destinos = DestinosTuristicos.objects.all()
    return render(request, 'destinos.html', {'destinos': destinos})