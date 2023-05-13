from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField('Nombre', max_length=60)
    correo = models.CharField('Correo', max_length=100)
    sueldo = models.DecimalField('Sueldo', max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre + ' | ' + self.correo + ' | ' + str(self.sueldo)