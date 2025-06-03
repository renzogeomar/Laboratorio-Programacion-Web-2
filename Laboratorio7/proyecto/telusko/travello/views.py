from django.shortcuts import render
from .models import DestinosTuristicos
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistroUsuarioForm
from django.contrib.auth.decorators import login_required
from .forms import DestinoForm
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        destinos = DestinosTuristicos.objects.all()
    else:
        destinos = []

    return render(request, 'index.html', {'dests': destinos})
def destinos(request):
    destinos = DestinosTuristicos.objects.all()
    return render(request, 'destinos.html', {'destinos': destinos})
def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('index')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})

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

@login_required
def listar_destinos(request):
    destinos = DestinosTuristicos.objects.all()
    return render(request, 'destinos/listar.html', {'destinos': destinos})

@login_required
def crear_destino(request):
    if request.method == 'POST':
        form = DestinoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_destinos')
    else:
        form = DestinoForm()
    return render(request, 'destinos/formulario.html', {'form': form, 'titulo': 'Añadir Destino'})

@login_required
def modificar_destino(request, id):
    destino = get_object_or_404(DestinosTuristicos, id=id)
    if request.method == 'POST':
        form = DestinoForm(request.POST, request.FILES, instance=destino)
        if form.is_valid():
            form.save()
            return redirect('listar_destinos')
    else:
        form = DestinoForm(instance=destino)
    return render(request, 'destinos/formulario.html', {'form': form, 'titulo': 'Modificar Destino'})

@login_required
def eliminar_destino(request, id):
    destino = get_object_or_404(DestinosTuristicos, id=id)
    if request.method == 'POST':
        destino.delete()
        return redirect('listar_destinos')
    return render(request, 'destinos/eliminar_confirmacion.html', {'destino': destino})