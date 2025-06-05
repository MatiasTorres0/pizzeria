from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import PedidoForm
from .models import Pedido

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