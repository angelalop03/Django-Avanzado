from django.urls import path
from .views import (
    AnimalListView,
    AnimalCreateView,
    AnimalDetailView,
    AnimalUpdateView,
    AnimalDeleteView,
)

urlpatterns = [
    path('', AnimalListView.as_view()),
    path('create/', AnimalCreateView.as_view()),
    path('<int:pk>/', AnimalDetailView.as_view()),
    path('<int:pk>/update/', AnimalUpdateView.as_view()),
    path('<int:pk>/delete/', AnimalDeleteView.as_view()),
]
