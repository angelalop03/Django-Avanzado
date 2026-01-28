from django.urls import path
from .views import (
    AdoptionListView,
    AdoptionCreateView,
    AdoptionDetailView,
    AdoptionUpdateView,
    AdoptionDeleteView,
)

from .api import request_adoption

urlpatterns = [
    path('adoptions/', AdoptionListView.as_view()),
    path('adoptions/create/', AdoptionCreateView.as_view()),
    path('adoptions/<int:pk>/', AdoptionDetailView.as_view()),
    path('adoptions/<int:pk>/update/', AdoptionUpdateView.as_view()),
    path('adoptions/<int:pk>/delete/', AdoptionDeleteView.as_view()),
    path('animals/<int:animal_id>/request-adoption/', request_adoption),
]
