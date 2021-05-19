from django.urls import reverse
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length= 50)

    def __str__(self):
        return self.category 
    
    def get_absolute_url(self):
        return reverse('blog')



class Blog(models.Model):
    blogPostName = models.CharField(max_length= 50)
    blogPostDate = models.DateTimeField()
    blogPost= RichTextField(blank = True, null=True)
    blogCategory = models.CharField(max_length= 250, null= True)
    def __str__(self):
        return self.blogPostName
    

    def get_absolute_url(self):
        return reverse('blog')

