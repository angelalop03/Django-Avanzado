from rest_framework.viewsets import ModelViewSet
from .models import Adopter
from adopters.serializer import AdopterSerializer

# Create your views here.
# ======== #
# ViewSets #
# ======== #

#(GET, POST, PUT, DELETE) /adopters/
class AdopterViewSet(ModelViewSet):
    queryset = Adopter.objects.all().order_by('-created_at')
    serializer_class = AdopterSerializer
    lookup_field = 'pk'
