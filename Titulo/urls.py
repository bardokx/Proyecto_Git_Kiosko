from django.urls import path
from . import views

urlpatterns = [
    path("", views.start_session),
    path("home/", views.homepage),
    path("virtual_row/", views.waiting_row),
    path("terms_and_conditions/", views.terms),
    path("payment/", views.pay),
    path("tienda/", views.catalogo),
]