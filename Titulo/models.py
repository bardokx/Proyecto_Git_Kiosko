from django.db import models

# Create your models here.
class Tiendas(models.Model):
    name = models.CharField(max_length=200)

class Productos(models.Model):
    name = models.CharField(max_length=200)
    tiempo = models.PositiveIntegerField()
    precio = models.PositiveIntegerField()
    tienda = models.ForeignKey(Tiendas, on_delete=models.CASCADE)

class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    rol = models.PositiveIntegerField()
    correo = models.CharField(max_length=200)
    telefono = models.PositiveIntegerField()
