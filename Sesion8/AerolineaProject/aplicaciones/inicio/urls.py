from django.urls import path
from . import views

urlpatterns = [
    path('inicio/index', views.index),
]