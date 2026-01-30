from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdopterViewSet

router = DefaultRouter()
router.register('adopters', AdopterViewSet, basename='adopters')

urlpatterns = [
    path('', include(router.urls)),
]
