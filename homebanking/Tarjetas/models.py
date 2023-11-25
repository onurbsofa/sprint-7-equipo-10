from django.db import models
from Clientes.models import Cliente
from Negocio.models import Marcatarjeta

# Create your models here.

class Tarjeta(models.Model):
    TIPO_CHOICES = [
        ('Credito', 'Credito'),
        ('Debito', 'Debito')
    ]

    def get_marca_choices(self):
        return [
            (Marcatarjeta.objects.get(marca='VISA'), 'Visa'),
            (Marcatarjeta.objects.get(marca='MASTERCARD'), 'Mastercard'),
            (Marcatarjeta.objects.get(marca='Amex'), 'Amex')
        ]

    numero = models.CharField(primary_key=True, blank=True, null=False, max_length=45)
    cvv = models.CharField(db_column='CVV', blank=True, null=True, max_length=45)  # Field name made lowercase.
    tipo = models.CharField(blank=True, null=True, max_length=45, choices=TIPO_CHOICES)
    marca = models.ForeignKey(Marcatarjeta, on_delete=models.CASCADE, db_column='marca', blank=True, null=True)
    fechaotorgamiento = models.DateField(db_column='fechaOtorgamiento', blank=True, null=True)  # Field name made lowercase.
    fechaexpiracion = models.DateField(db_column='fechaExpiracion', blank=True, null=True)  # Field name made lowercase.
    customer_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='customer_id')

    class Meta:
        managed = False
        db_table = 'tarjeta'