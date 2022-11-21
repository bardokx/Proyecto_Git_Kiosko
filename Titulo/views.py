from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.

def start_session(request):
    return render(request, 'login.html')

def homepage(request):
    return render(request, 'home.html')

def catalogo(request):
    return render(request, 'productos.html')

def waiting_row(request):
    return render(request, "row.html")

def terms(request):
    return render(request, "terms_conditions.html")

def pay(request):
    return render(request, "pay.html")