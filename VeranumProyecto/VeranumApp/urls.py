from django.urls import path
from . import views

urlpatterns = [
    # ... otras URLs de tu aplicación ...

    path('', views.buscar_habitaciones, name='buscar_habitaciones'),
    path('resultados_habitaciones/', views.resultados_habitaciones, name='resultados_habitaciones'),
    path('servicios/', views.servicios_subservicios, name='servicios'),
]