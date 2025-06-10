from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

class Pizza(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Pizza'
        verbose_name_plural = 'Pizzas'

class Pedido(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    pizza_solicitada = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    total_pedido = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.total_pedido = self.pizza_solicitada.precio * self.cantidad
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Pedido de {self.nombre_cliente} - {self.pizza_solicitada}"

class Valoracion(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    puntuacion = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

class Pago(models.Model):
    METODO_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia'),
    ]
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    metodo = models.CharField(max_length=20, choices=METODO_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=False)

class Notificacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.TextField()
    leida = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)