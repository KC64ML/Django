from rest_framework import serializers
from .models import LoginModels


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginModels
        fields = ['username', 'password']
