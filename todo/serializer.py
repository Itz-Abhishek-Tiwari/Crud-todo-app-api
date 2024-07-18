from rest_framework import serializers
from .models import Todos, MyUser

class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MyUser
        fields = ["email", "password"]

    def create(self, validated_data):
        user = MyUser.objects.create_user(**validated_data)
        return user
