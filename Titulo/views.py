from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Tiendas, Productos, Usuarios
# Create your views here.

def start_session(request):
    return render(request, 'login.html')

def homepage(request):
    tiendas = Tiendas.objects.all()
    return render(request, 'home.html', {
        'tiendas': tiendas
    })

def catalogo(request):
    productos = Productos.objects.all()
    return render(request, 'productos.html', {
        'productos': productos
    })

def agregar_producto(request, producto_id):
    carrito = carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect('Titulo:tienda')

def eliminar_producto(request, producto_id):
    carrito = carrito(request)
    producto = Productos.objects.get(id = producto_id)
    carrito.eliminar(producto)
    return redirect('Titulo:tienda')

def restar_producto(request, producto_id):
    carrito = carrito(request)
    producto = Productos.objects.get(id = producto_id)
    carrito.restar(producto)
    return redirect('Titulo:tienda')

def limpiar_carrito(request):
    carrito = carrito(request)
    carrito.limpiar()
    return redirect('Titulo:tienda')

def waiting_row(request):
    usuario = Usuarios.objects.all()
    return render(request, "row.html", {
        'usuario': usuario
    })

def terms(request):
    return render(request, "terms_conditions.html")

def pay(request):
    return render(request, "pay.html")

def admin_tienda(request):
    return render(request)