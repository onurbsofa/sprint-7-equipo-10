from datetime import datetime
from django.shortcuts import render, redirect
from django.views import View

from Clientes.models import Cliente
from .forms import SolicitudPrestamoForm
from .models import Prestamo
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class SolicitarPrestamo(LoginRequiredMixin, View):
    def get(self, request):
        form = SolicitudPrestamoForm()
        return render(request, 'solicitudPrestamo.html', {'form': form})

    def post(self, request):
        form = SolicitudPrestamoForm(request.POST)
        if form.is_valid():

            loan_type = form.cleaned_data.get('loan_type')
            loan_total = form.cleaned_data.get('loan_total')            
            loan_date = datetime.now().date().strftime('%Y-%m-%d')
            customer_id = Cliente.objects.get(customer_id=request.user.userprofile.customer_id)
            cliente = Cliente.objects.get(customer_id=request.user.userprofile.customer_id)
            customer_type = cliente.customer_type


            if customer_type == 'BLACK':
                preapproval_amount = 500000.00
            elif customer_type == 'GOLD':
                preapproval_amount = 300000.00
            else:  # CLASSIC
                preapproval_amount = 100000.00

            if loan_total > preapproval_amount:
                messages.error(request, 'Solicitud rechazada: El monto del préstamo excede el monto de preaprobación.')
                return render(request, 'solicitudPrestamo.html', {'form': form})


            Prestamo.objects.create(loan_type=loan_type, loan_date=loan_date, loan_total=loan_total, customer_id=customer_id)
            messages.success(request, 'Prestamo solicitado con exito')
            return redirect('home')
        
        else:
            print(form.errors)
            return render(request, 'solicitudPrestamo.html', {'form': form})
        
class PrestamosCliente(LoginRequiredMixin, View):
    def get(self, request):
        prestamos = Prestamo.objects.filter(customer_id=request.user.userprofile.customer_id)
        return render(request, 'prestamosCliente.html', {'prestamos': prestamos})