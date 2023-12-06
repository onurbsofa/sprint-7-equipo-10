from rest_framework import serializers
from django.contrib.auth.models import User
from Clientes.serializers import  ClienteSerializer
from Clientes.models import Cliente

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'customer_id')

class RegisterUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields 

    def create(self, validated_data):
        customer_id = validated_data.pop('customer_id')
        customer = Cliente.objects.get(id=customer_id) 
        user = User.objects.create_user(customer_id=customer, **validated_data)
        return user