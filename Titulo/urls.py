from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage),
    path("login/", views.start_session),
    path("virtual_row/", views.waiting_row),
    path("terms_and_conditions/", views.terms),
    path("payment/", views.pay),
]