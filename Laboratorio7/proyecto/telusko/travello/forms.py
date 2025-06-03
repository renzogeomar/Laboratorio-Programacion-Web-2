from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import DestinosTuristicos

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DestinoForm(forms.ModelForm):
    class Meta:
        model = DestinosTuristicos
        fields = '__all__'