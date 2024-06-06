from django import forms

class CrearCliente(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    
class CargarProductos(forms.Form):
    denominacion=forms.CharField(max_length=40)
    stock= forms.IntegerField()
    precio= forms.IntegerField()

class CrearCompra(forms.Form):
    orden= forms.IntegerField()
    total= forms.IntegerField()