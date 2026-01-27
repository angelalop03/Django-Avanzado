from django.db import models
from animals.models import Animal
from adopters.models import Adopter

# Create your models here.

class AdoptionRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'), ]
    
    adopter = models.ForeignKey(Adopter, on_delete=models.CASCADE, related_name='requests')
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='requests')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"AdoptionRequest {self.id} - {self.adopter.name} for {self.animal.name}"
    
    class Meta:
        ordering = ['-created_at']