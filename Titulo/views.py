from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Tiendas, Productos
# Create your views here.

def start_session(request):
    return render(request, 'login.html')

def homepage(request):
    return render(request, 'home.html')

def catalogo(request):
    productos = Productos.objects.all()
    return render(request, 'productos.html', {
        'productos': productos
    })

def waiting_row(request):
    return render(request, "row.html")

def terms(request):
    return render(request, "terms_conditions.html")

def pay(request):
    return render(request, "pay.html")

def admin_tienda(request):
    return render(request, "admin_tienda.html")