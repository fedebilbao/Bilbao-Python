from django.urls import path
from AppBilbao import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('perfil', views.perfil, name='perfil'),
    path('productos', views.productos, name='productos'),
    path('carrito', views.carrito, name='carrito'),
    path('crearCliente', views.crearCliente, name='crearCliente'),
    path('cargarProducto', views.cargarProducto, name='cargarProducto'),
    path('crearCompra', views.crearCompra, name='crearCompra'),
    path('buscarCliente', views.buscarCliente, name='buscarCliente'),
    path('buscar/', views.buscar, name='buscar'),
]