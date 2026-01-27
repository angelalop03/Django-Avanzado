from .models import Animal
from animals.serializer import AnimalSerializer
from rest_framework import status

from rest_framework import generics

# Create your views here.

# ======== #
# Generics #
# ======== #

#(GET) Listar todos los animales
class AnimalListView(generics.ListAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

#(POST) Crear un nuevo animal
class AnimalCreateView(generics.CreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

#(GET) Obtener un animal por su ID
class AnimalDetailView(generics.RetrieveAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

#(PUT) Actualizar un animal por su ID
class AnimalUpdateView(generics.UpdateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

#(DELETE) Eliminar un animal por su ID
class AnimalDeleteView(generics.DestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer