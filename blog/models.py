from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
    
class Post(models.Model):

    author = models.ForeignKey(User , on_delete=models.SET_NULL , null=True)
    image = models.ImageField(upload_to='blog/' , default='blog/default.jpg')
    # tag
    tags = TaggableManager()
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date',]

    def __str__(self):
        return f'{self.title} - {self.id}'
    
    def get_absolute_url(self):
        return reverse('blog:singleblog', kwargs={'pid':self.id})
    
    
