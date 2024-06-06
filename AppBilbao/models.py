from django.db import models

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

class Compra(models.Model):
    orden= models.IntegerField()
    total= models.IntegerField()
