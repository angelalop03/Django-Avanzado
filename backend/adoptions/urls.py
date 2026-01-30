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
    path('', AdoptionListView.as_view()),
    path('create/', AdoptionCreateView.as_view()),
    path('<int:pk>/', AdoptionDetailView.as_view()),
    path('<int:pk>/update/', AdoptionUpdateView.as_view()),
    path('<int:pk>/delete/', AdoptionDeleteView.as_view()),
    path('animals/<int:animal_id>/request-adoption/', request_adoption),
]
