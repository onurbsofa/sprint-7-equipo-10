from django.db import models

# Create your models here.

class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'

class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'

class AuditoriaCuenta(models.Model):
    old_id = models.IntegerField(primary_key=True, blank=True, null=False)  # The composite primary key (old_id, created_at) found, that is not supported. The first column is selected.
    new_id = models.IntegerField(blank=True, null=True)
    old_balance = models.IntegerField(blank=True, null=True)
    new_balance = models.IntegerField(blank=True, null=True)
    old_iban = models.IntegerField(blank=True, null=True)
    new_iban = models.IntegerField(blank=True, null=True)
    old_type = models.CharField(blank=True, null=True, max_length=45)
    new_type = models.CharField(blank=True, null=True, max_length=45)
    user_action = models.CharField(blank=True, null=True, max_length=45)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auditoria_cuenta'

class Marcatarjeta(models.Model):
    marca = models.CharField(primary_key=True, blank=True, null=False, max_length=45)

    class Meta:
        managed = False
        db_table = 'marcaTarjeta'

class Tipocliente(models.Model):
    tipo_cli = models.CharField(primary_key=True, blank=True, null=False, max_length=45)

    class Meta:
        managed = False
        db_table = 'tipoCliente'


class Tipocuenta(models.Model):
    tipo_cuen = models.CharField(primary_key=True, blank=True, null=False, max_length=45)

    class Meta:
        managed = False
        db_table = 'tipoCuenta'