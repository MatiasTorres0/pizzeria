from django import forms
from .models import Pizza, Pedido
from django.forms import ModelForm

class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ['nombre', 'descripcion', 'precio', 'disponible']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre_cliente', 'pizza_solicitada', 'cantidad']
        widgets = {
            'nombre_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'pizza_solicitada': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'})
        }
