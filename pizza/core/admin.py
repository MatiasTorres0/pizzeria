from django.contrib import admin
from . import models

admin.site.site_header = "Administración de Pizzas"
admin.site.site_title = "Panel de Administración de Pizzas"
admin.site.index_title = "Bienvenido al panel de administración de Pizzas"

@admin.register(models.Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'disponible']
    list_filter = ['disponible']
    search_fields = ['nombre']

@admin.register(models.Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre_cliente', 'pizza_solicitada', 'cantidad', 'total_pedido', 'fecha_pedido']
    list_filter = ['fecha_pedido']
    search_fields = ['nombre_cliente', 'pizza_solicitada']
    readonly_fields = ['fecha_pedido']
    ordering = ['-fecha_pedido']