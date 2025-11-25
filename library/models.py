from django.db import models
from django.contrib.auth.models import User  # <--- 1. Add this import

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    pdf_file = models.FileField(upload_to='books/', blank=True)
    
    cover_image = models.ImageField(upload_to='covers/', blank=True)

    external_link = models.URLField(blank=True)
    
    favorites = models.ManyToManyField(User, related_name='favorite_books', blank=True)

    def __str__(self):
        return self.title