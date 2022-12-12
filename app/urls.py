from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('registro/', registro, name="registro"),
    path('talleres/', talleres, name="talleres"),
    path('detalleT/<id_curso>', detalleT, name="detalleT"),
    path('postular/', postular, name="postular"),
    path('evaluar/', evaluar, name="evaluar"),
    path('detallePost/', detallePost, name="detallePost"),
    path('inscripcion/', inscripcion, name="inscripcion"),
    path('registroT/', registroT, name="registroT"),
    path('calificar/', calificar, name="calificar"),
    path('listarAM/', listarAM, name="listarAM"),
    path('modificar/<username>', modificar, name="modificar"),
    path('eliminarAdultoM/<username>', eliminarAdultoM, name="eliminarAdultoM"),
]