from django.shortcuts import render
from .models import DestinosTuristicos
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')
def destinos(request):
    destinos = DestinosTuristicos.objects.all()
    return render(request, 'destinos.html', {'destinos': destinos})
def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe.")
            return redirect('registro')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Usuario registrado correctamente.")
        return redirect('login')
    return render(request, 'registro.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
            return redirect('login')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')