from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Eventos

class EventoForm(forms.ModelForm):

    """
    Formulario para crear o editar eventos.
    Usa widgets Bootstrap para una mejor experiencia de usuario.
    """
    class Meta:
        model = Eventos
        fields = ['nombre', 'descripcion', 'fecha', 'organizador']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'organizador': forms.Textarea(attrs={'class': 'form-control' , 'rows': 1}),
        }

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']