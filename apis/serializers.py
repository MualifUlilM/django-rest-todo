from django.db.models import fields
from rest_framework import serializers
from todos import models
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user        

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'description', 'status')
        
        model = models.Todo