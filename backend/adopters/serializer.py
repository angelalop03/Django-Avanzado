from backend.adopters.models import Adopter

from rest_framework import serializers

class AdopterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adopter
        fields = ['id', 'name', 'email', 'phone_number', 'address', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']