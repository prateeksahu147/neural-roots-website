from django import forms
from .models import Blog
from .models import Category

# Dynamic way of make list from models
"""
choices= Category.objects.all().values_list('category', 'category')
choices_list = [cat for cat in choices ]
"""
"""
choices= [('Data Structure','Data Structure' ), ('Algorithms','Algorithms'),
             ('Machine Learning','Machine Learning'), ('Deep Learning','Deep Learning')]
"""
class BlogPostForm(forms.ModelForm):
    class Meta:
        model= Blog
        fields= ('blogPostName' ,'blogPostDate', 'blogPost', 'blogCategory' )
      
        widgets ={
            # all there fields are in BLog models
           'blogPostName': forms.TextInput(attrs={'class': 'form-control'}),
   
            'blogPost': forms.Textarea(attrs={'class': 'form-control'}),
            #'blogCategory': forms.Select(choices= choices_list, attrs={'class': 'form-control'})


       }