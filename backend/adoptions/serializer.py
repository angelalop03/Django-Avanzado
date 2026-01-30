from .models import AdoptionRequest
from rest_framework import serializers

class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptionRequest
        fields = ['id', 'adopter', 'animal', 'status', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']