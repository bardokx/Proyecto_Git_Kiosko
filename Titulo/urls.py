from django.urls import path
from . import views

urlpatterns = [
    path("", views.start_session, name="login"),
    path("home/", views.homepage, name="home"),
    path("virtual_row/", views.waiting_row, name="row"),
    path("terms_and_conditions/", views.terms, name="terms"),
    path("payment/", views.pay, name="payment"),
    path("tienda/", views.catalogo, name="shop"),
]
