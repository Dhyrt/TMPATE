from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import *



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'rut_usuario','username','first_name','s_nombre', 'last_name', 's_apellido','genero','email','tipo_usuario','password1','password2']