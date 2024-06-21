from django import forms
from .models import Avatar
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class CrearCliente(forms.Form):
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    
class CargarProductos(forms.Form):
    denominacion=forms.CharField(max_length=40)
    stock= forms.IntegerField()
    precio= forms.IntegerField()
    imagen = forms.ImageField()

class CrearCompra(forms.Form):
    orden= forms.IntegerField()
    total= forms.IntegerField()

class UserEditForm(UserChangeForm):
    password= forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model= User
        fields= ["first_name", "last_name", "email"]
    
    def clean_password2(self):
        password1= self.cleaned_data["password1"]
        password2= self.cleaned_data["password2"]

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
        
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen",]
