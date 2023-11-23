from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI', unique=True)  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'