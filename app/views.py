from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required,permission_required
from .forms import *
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

def index(request):
    cursos = Curso.objects.all()
    datos = {
        'listaTalleres' : cursos
    }
    return render(request, 'app/index.html', datos)

def registro(request):
    datos = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Usuario registrado con exito")
        datos["form"] = formulario
    return render(request, 'registration/registro.html', datos)

def postular(request):
    return render(request, 'app/postular.html')

def talleres(request):
    cursos = Curso.objects.all()
    datos = {
        'listaTalleres' : cursos
    }
    return render(request, 'app/talleres.html', datos)

def detalleT(request, id_curso):
    curso = Curso.objects.filter(id_curso=id_curso)
    datos = {
        'curso' : curso
    }
    return render(request, 'app/detalleT.html', datos)

def evaluar(request):
    return render(request, 'app/evaluar.html')

def detallePost(request):
    return render(request, 'app/detallePost.html')

def inscripcion(request):
    return render(request, 'app/inscripcion.html')

def registroT(request):
    return render(request, 'app/registroT.html')

def listarAM(request):
    if 'busq' in request.GET:
        busq = request.GET['busq']
        usuarios = User.objects.filter(rut_usuario__icontains=busq)
    else:
        usuarios = User.objects.all()
    datos = {
        'listaUsuarios' : usuarios
    }
    return render(request, 'app/listarAM.html', datos)

def modificar(request, username):
    usuarios = User.objects.get(username=username)
    datos = {
        'form' : CustomUserCreationForm(instance=usuarios)
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST, instance=usuarios)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Usuario modificado correctamente')
            datos['form'] = formulario
    return render(request, 'app/modificar.html', datos)

def eliminarAdultoM(request, username):
    usuarios = User.objects.get(username=username)
    usuarios.delete()
    return redirect(to="listarAM")

def calificar(request):
    return render(request, 'app/calificar.html')