from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.db import models
from django.http import JsonResponse
from rest_framework import serializers


CustomUser = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','email','organization','password')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            organization=validated_data['organization'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = models.EmailField()
    password = models.CharField()

    def validate(self, data):
        user = CustomUser.objects.get(email=data['email'])
        if(user.check_password(data['password'])):
            return user
        else:
            return JsonResponse({"attempted": make_password(data['password']), "actual": user.password})

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
