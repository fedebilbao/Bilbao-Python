from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"

class Productos(models.Model):
    denominacion=models.CharField(max_length=40)
    stock= models.IntegerField()
    precio= models.IntegerField()
    imagen = models.ImageField()
    def __str__(self):
        return f"{self.denominacion} - {self.stock} - {self.precio} - {self.imagen}"

class Compra(models.Model):
    orden= models.IntegerField()
    total= models.IntegerField()

class Avatar (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to="avatares", blank=True, null=True)

""" class ImagenProductos(models.Model):
    producto = models.OneToOneField(Productos, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="imagenes", blank=True, null=True) """
