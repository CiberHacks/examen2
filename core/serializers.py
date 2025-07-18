from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'is_completed', 'user']

class ToDoIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id']

class ToDoIDTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title']

class ToDoIDUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'user']



