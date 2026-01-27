from rest_framework import generics
from .models import AdoptionRequest
from serializer import AdoptionSerializer

# Create your views here.

#(GET) List all adoption requests
class AdoptionListView(generics.ListAPIView):
    queryset = AdoptionRequest.objects.all()
    serializer_class = AdoptionSerializer

#(POST) Create a new adoption request
class AdoptionCreateView(generics.CreateAPIView):
    queryset = AdoptionRequest.objects.all()
    serializer_class = AdoptionSerializer

#(GET) Retrieve a specific adoption request by ID
class AdoptionDetailView(generics.RetrieveAPIView):
    queryset = AdoptionRequest.objects.all()
    serializer_class = AdoptionSerializer

#(PUT) Update a specific adoption request by ID
class AdoptionUpdateView(generics.UpdateAPIView):
    queryset = AdoptionRequest.objects.all()
    serializer_class = AdoptionSerializer

#(DELETE) Delete a specific adoption request by ID
class AdoptionDeleteView(generics.DestroyAPIView):
    queryset = AdoptionRequest.objects.all()
    serializer_class = AdoptionSerializer

