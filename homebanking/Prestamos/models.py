from django.db import models
from Clientes.models import Cliente  
from django.core.validators import RegexValidator

class Prestamo(models.Model):
    TIPO_CHOICES = [
        ('PERSONAL', 'Personal'),
        ('HIPOTECARIO', 'Hipotecario'),
        ('PRENDARIO', 'Prendario')
    ]

    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField(max_length=20, choices=TIPO_CHOICES)
    loan_date = models.DateField()
    loan_total = models.IntegerField()
    customer_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='customer_id')

class Meta:
        managed = False
        db_table = 'prestamo'