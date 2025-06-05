from django import forms
from .models import pizza_lista, Pedido
from django.forms import ModelForm

class PizzaForm(ModelForm):
    class Meta:
        model = pizza_lista
        fields = ['nombre_pizza', 'ingredientes', 'precio', 'imagen', 'disponible']
        widgets = {
            'nombre_pizza': forms.TextInput(attrs={'class': 'form-control'}),
            'ingredientes': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ['nombre_cliente', 'pizza_solicitada', 'cantidad', 'estado']
        widgets = {
            'nombre_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'pizza_solicitada': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }
