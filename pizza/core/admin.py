from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_header = "Administración de Pizzas"
admin.site.site_title = "Panel de Administración de Pizzas"
admin.site.index_title = "Bienvenido al panel de administración de Pizzas"

admin.site.register(models.pizza_lista)
admin.site.register(models.Pedido)