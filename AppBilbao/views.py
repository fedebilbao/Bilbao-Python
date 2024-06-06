from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from .forms import CrearCliente, CargarProductos, CrearCompra
from .models import Cliente, Productos, Compra

# Create your views here.
def inicio(request):
    return render(request, "AppBilbao/inicio.html")
def perfil(request):
    return render(request, "AppBilbao/perfil.html")
def productos(request):
    return render (request, "AppBilbao/productos.html")
def carrito(request):
    return render(request, "AppBilbao/carrito.html")

def crearCliente(request):
    print("method: ", request.method)
    print("POST: ", request.POST)

    if request.method == "POST":
        nuevo_cliente = Cliente (nombre= request.POST["nombre"], apellido= request.POST["apellido"])
        nuevo_cliente.save()
        return render(request,"AppBilbao/inicio.html")
    
    else:
        miformulario = CrearCliente()
        return render(request,"AppBilbao/crearcliente.html", {"miformulario": miformulario})
    
def cargarProducto(request):
    print("method: ", request.method)
    print("POST: ", request.POST)

    if request.method == "POST":
        nuevo_producto = Productos (denominacion= request.POST["denominacion"], stock= request.POST["stock"], precio= request.POST["precio"])
        nuevo_producto.save()
        return render(request,"AppBilbao/inicio.html")
    
    else:
        miformulario = CargarProductos()
        return render(request,"AppBilbao/cargarproductos.html", {"miformulario": miformulario})
    
def crearCompra(request):
    print("method: ", request.method)
    print("POST: ", request.POST)

    if request.method == "POST":
        nueva_compra = Compra (orden= request.POST["orden"], total= request.POST["total"])
        nueva_compra.save()
        return render(request,"AppBilbao/inicio.html")
    
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
