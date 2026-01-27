from django.db import models

# Create your models here.

class Animal(models.Model):
    SPECIES_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('other', 'Other'),]
    
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('adopted', 'Adopted'),]
    
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=10, choices=SPECIES_CHOICES)
    age= models.PositiveIntegerField(null=True, blank=True)
    vaccinated = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.species})"
    
    class Meta:
        ordering = ['-created_at']
