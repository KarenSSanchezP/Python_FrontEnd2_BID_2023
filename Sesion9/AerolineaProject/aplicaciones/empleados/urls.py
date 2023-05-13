from django.urls import path
from . import views

app_name = 'empleados_app'
urlpatterns = [
    path('empleado/lista-empleados/', views.lista_empleados, name='lista-empleados'),
    path('empleado/crear-empleado/', views.CrearEmpleado.as_view(), name='crear-empleado'),
    path(
    'empleado/modificar-empleado/<pk>/', 
    views.ModificarEmpleado.as_view(), 
    name='modificar-empleado'),
    path(
    'empleado/eliminar-empleado/<pk>/', 
    views.EliminarEmpleado.as_view(), 
    name='eliminar-empleado'),
]