# serializers.py
from rest_framework import serializers

class AboutSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()

class MyserviceSerializer(serializers.Serializer):
    email = serializers.EmailField()
    

