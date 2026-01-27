from django.urls import path
from .views import (
    AnimalListView,
    AnimalCreateView,
    AnimalDetailView,
    AnimalUpdateView,
    AnimalDeleteView,
)

urlpatterns = [
    path('animals/', AnimalListView.as_view()),
    path('animals/create/', AnimalCreateView.as_view()),
    path('animals/<int:pk>/', AnimalDetailView.as_view()),
    path('animals/<int:pk>/update/', AnimalUpdateView.as_view()),
    path('animals/<int:pk>/delete/', AnimalDeleteView.as_view()),
]
