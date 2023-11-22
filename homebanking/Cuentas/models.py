from django.db import models

# Create your models here.

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    tipo = models.CharField(blank=True, null=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'cuenta'