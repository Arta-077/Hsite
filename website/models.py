from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date',]

    def __str__(self):
        return f'{self.name} - {self.id}'


class Newsletter(models.Model):
    Email = models.EmailField()

    def __str__(self):
        return f'{self.Email}'
    
    








