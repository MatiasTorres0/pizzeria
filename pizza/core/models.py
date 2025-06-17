from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre

class Pizza(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.ImageField(upload_to='pizzas/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizzas'

class Pedido(models.Model):
    nombre_cliente = models.CharField(max_length=100, verbose_name="Nombre del Cliente")
    pizza_solicitada = models.ForeignKey(Pizza, on_delete=models.CASCADE, verbose_name="Pizza")
    cantidad = models.PositiveIntegerField(default=1)
    total_pedido = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_pedido = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_pedido = self.pizza_solicitada.precio * self.cantidad
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido de {self.nombre_cliente} - {self.pizza_solicitada}"

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['-fecha_pedido']