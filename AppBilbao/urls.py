from django.urls import path
from django.contrib.auth.views import LogoutView
from AppBilbao import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('perfil', views.perfil, name='perfil'),
    path('productos', views.productos, name='productos'),
    path('carrito', views.carrito, name='carrito'),
    path('crearCliente', views.crearCliente, name='crearCliente'),
    path('cargarProducto', views.cargarProducto, name='cargarProducto'),
    path('eliminarProducto/<int:id>', views.eliminarProducto, name='eliminarProducto'),
    path('editarProducto/<int:id>', views.editarProducto, name='editarProducto'),
    path('crearCompra', views.crearCompra, name='crearCompra'),
    path('buscarCliente', views.buscarCliente, name='buscarCliente'),
    path('buscar/', views.buscar, name='buscar'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('detailProducto/<int:id>', views.detailProducto, name='detailProducto'),
    path('login/', views.loginform, name='login'),
    path('register/', views.registerform, name='register'),
    path('logout/', LogoutView.as_view(template_name="AppBilbao/logout.html"), name='logout'),
    path('editarPerfil/', views.edituser, name='editarPerfil'),
    path('agregarAvatar/', views.agregaravatar, name='agregarAvatar'),
]