# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuditoriaCuenta(models.Model):
    old_id = models.IntegerField(primary_key=True, blank=True, null=True)  # The composite primary key (old_id, created_at) found, that is not supported. The first column is selected.
    new_id = models.IntegerField(blank=True, null=True)
    old_balance = models.IntegerField(blank=True, null=True)
    new_balance = models.IntegerField(blank=True, null=True)
    old_iban = models.IntegerField(blank=True, null=True)
    new_iban = models.IntegerField(blank=True, null=True)
    old_type = models.CharField(blank=True, null=True)
    new_type = models.CharField(blank=True, null=True)
    user_action = models.CharField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auditoria_cuenta'


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI', unique=True)  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    tipo = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta'


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


class Marcatarjeta(models.Model):
    marca = models.CharField(primary_key=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'marcaTarjeta'


class Movimientos(models.Model):
    numero_cuenta = models.IntegerField(blank=True, null=True)
    monto = models.FloatField(blank=True, null=True)
    tipo_operacion = models.TextField(blank=True, null=True)
    hora = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'movimientos'


class NuevaCuenta(models.Model):
    account_id = models.AutoField(primary_key=True, blank=True, null=True)
    customer = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)
    iban = models.TextField(blank=True, null=True)
    tipo_cuenta = models.ForeignKey('Tipocuenta', models.DO_NOTHING, db_column='tipo_cuenta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nueva_cuenta'


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sucursal'


class Tarjeta(models.Model):
    numero = models.CharField(primary_key=True, blank=True, null=True)
    cvv = models.CharField(db_column='CVV', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(blank=True, null=True)
    marca = models.ForeignKey(Marcatarjeta, models.DO_NOTHING, db_column='marca', blank=True, null=True)
    fechaotorgamiento = models.DateField(db_column='fechaOtorgamiento', blank=True, null=True)  # Field name made lowercase.
    fechaexpiracion = models.DateField(db_column='fechaExpiracion', blank=True, null=True)  # Field name made lowercase.
    customer = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarjeta'


class Tipocliente(models.Model):
    tipo_cli = models.CharField(primary_key=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoCliente'


class Tipocuenta(models.Model):
    tipo_cuen = models.CharField(primary_key=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoCuenta'
