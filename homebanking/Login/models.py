from django.contrib.auth.models import  User
from django.db import models

from Clientes.models import Cliente

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_column='user_id')
    customer = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='customer_id')
