from django.urls import path
from . import views

urlpatterns = [
    path('inicio/index', views.index),
    path('inicio/consultar-precios', views.consultar_precios),
    path('inicio/consultar-precios-js', views.consultar_precios_js),
    path('inicio/ejercicio1-api', views.ejercicio1_api),
]