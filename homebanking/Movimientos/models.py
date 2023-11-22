from django.db import models

# Create your models here.

class Movimientos(models.Model):
    numero_cuenta = models.IntegerField(blank=True, null=True)
    monto = models.FloatField(blank=True, null=True)
    tipo_operacion = models.TextField(blank=True, null=True)
    hora = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'movimientos'