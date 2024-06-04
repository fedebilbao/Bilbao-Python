from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)

class Productos(models.Model):
    denominación=models.CharField(max_length=40)
    stock= models.IntegerField()
    precio= models.IntegerField()

class Compra(models.Model):
    orden= models.IntegerField()
    total= models.IntegerField()
