from django.db import models
from Clientes.models import Cliente  
from django.core.validators import RegexValidator

class Prestamo(models.Model):
    TIPO_CHOICES = [
        ('hipotecario', 'Hipotecario'),
        ('personal', 'Personal'),
        ('prendario', 'Prendario'),
    ]

    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField(max_length=20, choices=TIPO_CHOICES)
    loan_date = models.DateField()
    loan_total = models.CharField(
        max_length=8,
        validators=[
            RegexValidator(r'^[0-9]{8}$'),
        ])
    customer = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Meta:
        managed = False
        db_table = 'prestamo'
       