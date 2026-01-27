from backend.adoptions.models import Adoption
from rest_framework import serializers

class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = ['id', 'adopter', 'pet', 'adoption_date', 'status', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']