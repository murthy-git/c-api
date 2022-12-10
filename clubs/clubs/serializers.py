from rest_framework import serializers
from .models import Club

class clubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name', 'description', 'created_by', 'created_at']
        