from django.db import models
from datetime import datetime


class Type(models.Model):
    name=models.CharField(max_length=30, verbose_name='Tipo: ')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Tipo'
        db_table='Tipo'
        ordering=['id']
class Empleado(models.Model):
    type=models.ForeignKey(Type, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=30, verbose_name="Nombre: ")
    apellido=models.CharField(max_length=30, verbose_name="Apellido: ")
    descripcion=models.TextField()
    fechaReg=models.DateField(default=datetime.now, verbose_name="Fecha de registro: ")
    edad=models.PositiveIntegerField(default=0)
    salario=models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    avatar=models.ImageField(upload_to="avatar/%Y/%m/%d", null=True, blank=True)


    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name='Empleado'
        db_table='Empleado'
        ordering=['id']

