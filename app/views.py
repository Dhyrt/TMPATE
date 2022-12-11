from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required,permission_required
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def login(request):
    return render(request, 'registration/login.html')

def registro(request):
    datos ={
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user= authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="index")
        datos["form"] = formulario
    return render(request, 'registration/registro.html', datos)

def postular(request):
    return render(request, 'app/postular.html')

def talleres(request):
    return render(request, 'app/talleres.html')

def detalleT(request):
    return render(request, 'app/detalleT.html')

def evaluar(request):
    return render(request, 'app/evaluar.html')

def detallePost(request):
    return render(request, 'app/detallePost.html')

def inscripcion(request):
    return render(request, 'app/inscripcion.html')

def registroT(request):
    return render(request, 'app/registroT.html')

