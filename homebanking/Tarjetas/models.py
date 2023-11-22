from django.db import models
from Clientes.models import Cliente
from Negocio.models import Marcatarjeta

# Create your models here.

class Tarjeta(models.Model):
    numero = models.CharField(primary_key=True, blank=True, null=False, max_length=45)
    cvv = models.CharField(db_column='CVV', blank=True, null=True, max_length=45)  # Field name made lowercase.
    tipo = models.CharField(blank=True, null=True, max_length=45)
    marca = models.ForeignKey(Marcatarjeta, models.DO_NOTHING, db_column='marca', blank=True, null=True)
    fechaotorgamiento = models.DateField(db_column='fechaOtorgamiento', blank=True, null=True)  # Field name made lowercase.
    fechaexpiracion = models.DateField(db_column='fechaExpiracion', blank=True, null=True)  # Field name made lowercase.
    customer = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarjeta'