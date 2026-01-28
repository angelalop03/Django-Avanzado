from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from animals.models import Animal
from adopters.models import Adopter
from .models import AdoptionRequest

@api_view(['POST'])
def request_adoption(request, animal_id):
    try:
        animal = Animal.objects.get(id=animal_id)
    except Animal.DoesNotExist:
        return Response({"error": "Animal no existe"}, status=404)

    if animal.status != "available":
        return Response({"error": "Animal no disponible"}, status=400)

    adopter_id = request.data.get("adopter_id")

    try:
        adopter = Adopter.objects.get(id=adopter_id)
    except Adopter.DoesNotExist:
        return Response({"error": "Adopter no existe"}, status=404)

    adoption = AdoptionRequest.objects.create(
        animal=animal,
        adopter=adopter
    )

    animal.status = "reserved"
    animal.save()

    return Response(
        {
            "message": "Solicitud de adopción creada",
            "adoption_id": adoption.id,
            "animal_status": animal.status
        },
        status=status.HTTP_201_CREATED
    )
