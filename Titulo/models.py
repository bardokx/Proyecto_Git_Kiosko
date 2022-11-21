from django.db import models

# Create your models here.
class Tiendas(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Productos(models.Model):
    name = models.CharField(max_length=200)
    tiempo = models.PositiveIntegerField()
    precio = models.PositiveIntegerField()
    tienda = models.ForeignKey(Tiendas, on_delete=models.CASCADE)

class Usuarios(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    n_fila = models.PositiveIntegerField()
    def __str__(self):
        return self.nombre
