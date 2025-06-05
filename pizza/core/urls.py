from .views import inicio, pedidos
from django.urls import path

urlpatterns = [
    path('', inicio, name='inicio'),
    path('pedidos/', pedidos, name='pedidos'),
]