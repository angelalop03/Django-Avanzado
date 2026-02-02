from rest_framework.viewsets import ModelViewSet
from .models import Adopter
from adopters.serializer import AdopterSerializer
from rest_framework import generics

# Create your views here.
# ======== #
# ViewSets #
# ======== #

#(GET, POST, PUT, DELETE) /adopters/
class AdopterViewSet(ModelViewSet):
    queryset = Adopter.objects.all().order_by('-created_at')
    serializer_class = AdopterSerializer
    lookup_field = 'pk'

# ========= #
# Generics  #
# ========= #

#(GET) Listar todos los adoptantes
class AdopterListView(generics.ListAPIView):
    queryset = Adopter.objects.all()
    serializer_class = AdopterSerializer

#(POST) Crear un nuevo adoptante
class AdopterCreateView(generics.CreateAPIView):
    queryset = Adopter.objects.all()
    serializer_class = AdopterSerializer


#(PUT) Actualizar un adoptante por su ID
class AdopterUpdateView(generics.UpdateAPIView):
    queryset = Adopter.objects.all()
    serializer_class = AdopterSerializer

#(DELETE) Eliminar un adoptante por su ID
class AdopterDeleteView(generics.DestroyAPIView):
    queryset = Adopter.objects.all()
    serializer_class = AdopterSerializer


