from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("start_session/", views.start_session),
]