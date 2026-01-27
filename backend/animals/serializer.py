from rest_framework import serializers
from .models import Animal

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'name', 'species', 'age', 'vaccinated', 'status', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_age(self, value):
        if value is not None and value < 0:
            raise serializers.ValidationError("Age cannot be negative.")
        return value