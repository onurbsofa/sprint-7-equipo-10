from rest_framework import serializers
from django.contrib.auth.models import User
from Clientes.serializers import  ClienteSerializer
from Clientes.models import Cliente
from Login.models import UserProfile 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class RegisterUserSerializer(UserSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all())

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('customer',)

    def create(self, validated_data):
        customer = validated_data.pop('customer')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, customer=customer)  # Create a UserProfile instance
        return user