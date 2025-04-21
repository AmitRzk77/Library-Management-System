from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    adress = models.CharField(max_length=255, null=True,blank=True)
    email = models.EmailField(max_length=255,null=True)
    contact = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name