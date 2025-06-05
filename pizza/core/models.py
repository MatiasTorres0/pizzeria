from django.db import models

# Create your models here.
class pizza_lista(models.Model):
    nombre_pizza = models.CharField(max_length=100)
    ingredientes = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    imagen = models.ImageField(upload_to='pizzas/', null=True, blank=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_pizza
    
class Pedido(models.Model):
    ESTADO = (
        ('Pendiente', 'Pendiente'),
        ('En preparación', 'En preparación'),
        ('Listo para entregar', 'Listo para entregar'),
        ('Entregado', 'Entregado'),
        ('Cancelado', 'Cancelado'),
    )
    nombre_cliente = models.CharField(max_length=100)
    pizza_solicitada = models.ForeignKey(pizza_lista, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, default='Pendiente', choices=ESTADO)
    total_pedido = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)
    def __str__(self):
        return f"{self.nombre_cliente} - {self.pizza_solicitada.nombre_pizza} ({self.cantidad})"