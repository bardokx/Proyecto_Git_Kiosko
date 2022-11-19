from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def homepage(request):
    return render(request, 'home.html')

def start_session(request):
    return render(request, 'login.html')

def waiting_row(request):
    return render(request, "row.html")

def terms(request):
    return render(request, "terms_conditions.html")

def pay(request):
    return render(request, "pay.html")