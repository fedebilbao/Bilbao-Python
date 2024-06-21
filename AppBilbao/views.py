from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from .forms import CrearCliente, CargarProductos, CrearCompra, UserEditForm, AvatarForm
from .models import Cliente, Productos, Compra, Avatar
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
""" from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
 """
# Create your views here.
def inicio(request):
    return render(request, "AppBilbao/inicio.html")

@login_required()
def perfil(request):
    avatar = Avatar.objects.get(user=request.user.id)
    return render(request, "AppBilbao/perfil.html", {"url": avatar.imagen.url})
def productos(request):
    misProductos = Productos.objects.all()

    return render (request, "AppBilbao/productos.html", {"productos":misProductos})
def carrito(request):
    return render(request, "AppBilbao/carrito.html")

def crearCliente(request):
    print("method: ", request.method)
    print("POST: ", request.POST)

    if request.method == "POST":
        miFormulario = CrearCliente(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            
            nuevo_cliente = Cliente (nombre= data["nombre"], apellido= data["apellido"])
            nuevo_cliente.save()
            return render(request,"AppBilbao/inicio.html", {"message": f"Cliente {nuevo_cliente} creado con éxito"})
        else:
            return render (request, "AppBilbao/inicio.html", {"message": "Datos Inválidos"})
    
    else:
        miformulario = CrearCliente()
        return render(request,"AppBilbao/crearcliente.html", {"miformulario": miformulario})

@login_required()   
def cargarProducto(request):
    print("method: ", request.method)
    print("POST: ", request.POST)

    if request.method == "POST":
        nuevo_producto = Productos (denominacion= request.POST["denominacion"], stock= request.POST["stock"], precio= request.POST["precio"], imagen=request.POST["imagen"])
        nuevo_producto.save()
        return render(request,"AppBilbao/productos.html", {"message": f"Producto {nuevo_producto} creado correctamente"})
    
    else:
        miformulario = CargarProductos()
        return render(request,"AppBilbao/cargarproductos.html", {"miformulario": miformulario})

@login_required()
def eliminarProducto(request, id):
        if request.method == "POST" :

            producto = Productos.objects.get (id=id)
            producto.delete()

            misProductos = Productos.objects.all()
            return render (request, "AppBilbao/productos.html", {"productos":misProductos})

@login_required()
def editarProducto (request, id):

    if request.method == "POST":
            producto = Productos.objects.get(id=id)
            producto.denominacion= request.POST["denominacion"]
            producto.stock= request.POST["stock"]
            producto.precio= request.POST["precio"]
            producto.imagen=request.POST["imagen"]
            producto.save()
            return render(request,"AppBilbao/productos.html")
    
    else:
        producto = Productos.objects.get(id=id)
        miformulario = CargarProductos(initial={
            "denominacion": producto.denominacion,
            "stock": producto.stock,
            "precio": producto.precio,
            "imagen": producto.imagen,
        })
        return render(request,"AppBilbao/editarproductos.html", {"miformulario": miformulario, "id":producto.id})

def detailProducto (request, id):
    producto = Productos.objects.get(id=id)

    return render (request, "AppBilbao/productodetail.html", {"producto":producto})

def crearCompra(request):
    print("method: ", request.method)
    print("POST: ", request.POST)

    if request.method == "POST":
        nueva_compra = Compra (orden= request.POST["orden"], total= request.POST["total"])
        nueva_compra.save()
        return render(request,"AppBilbao/inicio.html", {"message": f"compra {nueva_compra} creada correctamente"})
    
    else:
        miformulario = CrearCompra()
        return render(request,"AppBilbao/crearcompra.html", {"miformulario": miformulario})
    
def buscarCliente(request):
    return render(request, "AppBilbao/buscarcliente.html",{})

def buscar(request):
    if request.GET["apellido"]:
        apellido = request.GET["apellido"]
        nombre = Cliente.objects.get(apellido=apellido)
        return render(request, "AppBilbao/resultadosBusqueda.html", {"nombre": nombre, "apellido": apellido})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

def nosotros (request):
    return render(request, "AppBilbao/nosotros.html")

def loginform (request):

    if request.method == "POST":
        miFormulario = AuthenticationForm(request, data=request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            
            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:
                login(request, user)
                return render (request, "AppBilbao/inicio.html", {"message": f"Bienvenido {usuario}"})
            else:

                return render(request,"AppBilbao/inicio.html", {"message": "Datos erroneos"})
        else:
            return render (request, "AppBilbao/inicio.html", {"message": "Datos Inválidos"})
    
    else:
        miformulario = AuthenticationForm()
        return render(request,"AppBilbao/login.html", {"miformulario": miformulario})
    
def registerform (request):
    if request.method == "POST":
        miFormulario = UserCreationForm(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            
            usuario = data["username"]
            miFormulario.save()
            return render(request,"AppBilbao/inicio.html", {"message": f"Usuario {usuario} creado con éxito"})
        else:
            return render (request, "AppBilbao/inicio.html", {"message": "Datos Inválidos"})
    
    else:
        miformulario = UserCreationForm()
        return render(request,"AppBilbao/register.html", {"miformulario": miformulario})

@login_required()
def edituser (request):

    usuario = request.user

    if request.method == "POST":
            miFormulario = UserEditForm(request.POST, instance= request.user)
            
            if miFormulario.is_valid():
                data = miFormulario.cleaned_data
                usuario.first_name= data["first_name"]
                usuario.last_name= data["last_name"]
                usuario.email= data["email"]
                usuario.set_password(data["password1"])
                usuario.save()
                return render(request,"AppBilbao/inicio.html", {"message": "Datos actualizados con éxito"})
            
            else:
                return render(request,"AppBilbao/editarperfil.html", {"miformulario": miFormulario})
    
    else:
        miformulario = UserEditForm(instance= request.user)

        return render(request,"AppBilbao/editarperfil.html", {"miformulario": miformulario})


def agregaravatar (request):
    if request.method == "POST":
            miFormulario = AvatarForm(request.POST, request.FILES)
            
            if miFormulario.is_valid():
                data = miFormulario.cleaned_data
                avatar = Avatar(user= request.user, imagen = data["imagen"])
                avatar.save()
                return render(request,"AppBilbao/inicio.html", {"message": "Avatar cargado con éxito"})
            
            else:
                return render(request,"AppBilbao/inicio.html", {"message": "Datos inválidos"})
    
    else:
        miformulario = AvatarForm()

        return render(request,"AppBilbao/agregaravatar.html", {"miformulario": miformulario})
    