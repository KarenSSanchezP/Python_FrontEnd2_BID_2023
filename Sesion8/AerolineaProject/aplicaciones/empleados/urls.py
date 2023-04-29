from django.urls import path
from . import views

urlpatterns = [
    path('empleado/lista-empleados/', views.lista_empleados),
]