from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('login/', login, name="login"),
    path('registro/', registro, name="registro"),
    path('talleres/', talleres, name="talleres"),
    path('detalleT/', detalleT, name="detalleT"),
    path('postular/', postular, name="postular"),
    path('evaluar/', evaluar, name="evaluar"),
]