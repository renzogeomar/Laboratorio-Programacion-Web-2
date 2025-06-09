from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail('Hello from Django',
    'Hola, este es un mensaje de prueba enviado desde Django.',
    'renzogeomarm@gmail.com',
    ['lotoj89494@pngzero.com'],
    fail_silently=False)

    return render(request,'send/index.html')

