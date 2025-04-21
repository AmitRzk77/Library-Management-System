from django.db import models
from book.models import Book

# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    email = models.EmailField(max_length=255)
    review = models.DateField(max_length=2000)
    rating = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name