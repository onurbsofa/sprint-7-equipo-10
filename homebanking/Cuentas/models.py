from django.db import models

from Clientes.models import Cliente

# Create your models here.

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='customer_id')
    balance = models.IntegerField()
    iban = models.TextField()
    tipo = models.CharField(blank=True, null=True, max_length=45)
    

    class Meta:
        managed = False
        db_table = 'cuenta'