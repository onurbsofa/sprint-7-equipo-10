from django.shortcuts import render, redirect
from django.http import Http404 
from .forms import SolicitudPrestamoForm
from .models import Prestamo
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def solicitud_prestamo(request):
    if request.method == 'POST':
        form = SolicitudPrestamoForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            
            solicitud.customer = request.user.cliente

            tipo_cliente = obtener_tipo_cliente(request.user) 
            monto_maximo = obtener_monto_maximo(tipo_cliente)

            monto_solicitado = int(solicitud.loan_total)

            if monto_solicitado <= monto_maximo:
                solicitud.aprobada = True
            else:
                solicitud.aprobada = False

            solicitud.save()
            messages.success(request, 'La solicitud de préstamo fue enviada con éxito.')
            return redirect('inicio.html')  
        else:
            messages.error(request, 'Hubo un error en el formulario. Por favor, revise los datos e inténtelo nuevamente.')
            raise Http404("Página no encontrada")

    else:
        form = SolicitudPrestamoForm()

    return render(request, 'solicitud_prestamo.html', {'form': form})

def obtener_tipo_cliente(usuario):
    if usuario.is_authenticated:
        return usuario.tipo_cliente
    else:
        return 'None'

def obtener_monto_maximo(tipo_cliente):
    if tipo_cliente == 'BLACK':
        return 500000
    elif tipo_cliente == 'GOLD':
        return 300000
    elif tipo_cliente == 'CLASSIC':
        return 100000
    else:
        return 0
