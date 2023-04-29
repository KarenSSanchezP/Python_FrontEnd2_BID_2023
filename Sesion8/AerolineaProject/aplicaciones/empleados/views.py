from django.shortcuts import render
from .models import Empleado

# Create your views here.
def lista_empleados(request):
    #Diccionario 'datos', guardaremos una lista de empleados ordenador por nombre
    datos = {
        'lista': Empleado.objects.all().order_by('nombre'),
        'titulo': 'Lista de empleados',
    }
    return render(request, 'empleados/lista-empleados2.html', datos)

