from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('menu/', views.menu, name='menu'),
    path('carrito/', views.carrito, name='carrito'),
]