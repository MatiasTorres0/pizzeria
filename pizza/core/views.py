from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Count
from django.db.models.functions import TruncDate

from .forms import PedidoForm
from .models import Pedido, Pizza, Categoria

# Create your views here.
def inicio(request):
    return render(request, 'core/inicio.html')

def pedidos(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, '¡Pedido creado exitosamente!')
                return redirect('pedidos')
            except Exception as e:
                messages.error(request, f'Error al crear el pedido: {str(e)}')
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = PedidoForm()
    
    data = {
        'pedidos': form,
        'pedidos_list': Pedido.objects.all().order_by('-fecha_pedido')
    }
    return render(request, 'core/pedidos.html', data)

def dashboard(request):
    ventas_diarias = Pedido.objects.annotate(
        fecha=TruncDate('fecha_pedido')
    ).values('fecha').annotate(
        total=Sum('total_pedido'),
        cantidad=Count('id')
    ).order_by('-fecha')
    
    return render(request, 'core/dashboard.html', {'ventas': ventas_diarias})

def menu(request):
    categorias = Categoria.objects.all()
    pizzas = Pizza.objects.filter(disponible=True)
    return render(request, 'core/menu.html', {
        'categorias': categorias,
        'pizzas': pizzas
    })

@login_required
def carrito(request):
    return render(request, 'core/carrito.html')

@login_required
def perfil(request):
    pedidos = Pedido.objects.filter(cliente=request.user).order_by('-fecha_pedido')
    return render(request, 'core/perfil.html', {'pedidos': pedidos})

def contacto(request):
    return render(request, 'core/contacto.html')

def about(request):
    return render(request, 'core/about.html')