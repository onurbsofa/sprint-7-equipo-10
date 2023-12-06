"""
URL configuration for homebanking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Clientes.views import DatosCliente
from Prestamos.views import PrestamosCliente, SolicitarPrestamo
from Cuentas.views import CuentasCliente, SolicitarCuenta
from Login.views import LoginView, LogoutView, RegisterView, HomeView,  LoginAPIView
from Tarjetas.views import SolicitarTarjeta, TarjetasCliente
from Clientes.views import DatosClienteList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
    path('usuario/', DatosCliente.as_view(), name='datosCliente'),
    path('cuentas/', CuentasCliente.as_view(), name='cuentasCliente'),
    path('cuentas/solicitar', SolicitarCuenta.as_view(), name='solicitudCuenta'),
    path('prestamos/', PrestamosCliente.as_view(), name='prestamosCliente'),
    path('prestamos/solicitar', SolicitarPrestamo.as_view(), name='solicitudPrestamo'),
    path('tarjetas/', TarjetasCliente.as_view(), name='tarjetasCliente'),
    path('tarjetas/solicitar', SolicitarTarjeta.as_view(), name='solicitudTarjeta'),
    path('api/clientes', DatosClienteList.as_view(), name='api-clientes'),
    path('api-auth/', LoginAPIView.as_view(), name='api-login'),
]
