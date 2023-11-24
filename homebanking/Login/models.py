from django.contrib.auth.models import  User
from django.db import models

class UserProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, db_column='user_id')
    customer_id = models.CharField(max_length=255)
