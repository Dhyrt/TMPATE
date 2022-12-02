from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def login(request):
    return render(request, 'app/login.html')

def registro(request):
    return render(request, 'app/registro.html')

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