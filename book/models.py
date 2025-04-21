from django.db import models
from author.models import Author
from genre.models import Genre
from volume.models import Volume
from publication.models import Publication
from django.utils.text import slugify
import uuid
from django.contrib.auth.models import AbstractUser







class Book(models.Model):
    TYPE_CHOICES = {
       ('hardcover' , 'Hardcover'),
        ('paperback' , 'Paperback'),
    }

 #   book_type = models.CharField(max_length=10, choice =TYPE_CHOICES)
# Create your models here.

    name = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='books_author')
    book_type = models.CharField(max_length=10, choices =TYPE_CHOICES, default='hardcover')
    genre =  models.ForeignKey(Genre, on_delete=models.CASCADE,related_name='books_genre')
    slug = models.SlugField(max_length=255, editable=False)
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE,related_name='books_volume')
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE,related_name='books_publication')
    publication_year = models. PositiveBigIntegerField(null = True, blank=True)
    isbn =  models.CharField(max_length=13,unique= True)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='pdf-files/', null=True,blank=True)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True,null=True)
    published_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slog = models.CharField(max_length=255, blank=True, null=True)
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    


    def __str__(self):  #book ko title anusar dekhhiyos ntra object ma aauxa
        return self.name
    

    def save(self, *args, **kwargs):
        if not self.slog:
            self.slog = f'{slugify(self.name)}-{str(self.public_id)[1:5]}{str(self.public_id)[-1:-5]}'
            super().save(*args, **kwargs)




