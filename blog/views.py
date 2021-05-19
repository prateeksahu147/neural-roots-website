from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView
from django.views.generic.detail import DetailView
from .models import Blog, Category
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from .forms import BlogPostForm
# Create your views here.

def viewCategoryPost(request, cats):
    """
    this will give category wise blogs 
    here cats is category that we passed in url
    
    """
    categoryPost=Blog.objects.filter(blogCategory=cats)
    return render(request,'blog/categoryWisePost.html' , {'cats':cats,'categoryPost':categoryPost ,})

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        """
        this code for pagination
        https://stackoverflow.com/questions/5907575/how-do-i-use-pagination-with-django-class-based-generic-listviews
        source code
        """
        cat_menu= Category.objects.all() 
        context = super(BlogListView, self).get_context_data(*args, **kwargs) 
        list_exam = Blog.objects.all()
        paginator = Paginator(list_exam, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)
        context['list_exams', 'cat_menu'] = file_exams, cat_menu
        return context
    
    def get_context_data(self, *args, **kwargs):
        """
        we add another context function for adding category menu
        in page, we fatch 'Category' class from models
        """
        context = super(BlogListView, self).get_context_data(*args, **kwargs) 
        cat_menu= Category.objects.all() 
        context[ 'cat_menu'] = cat_menu
        
        return context


class BlogDetailView(DetailView):
        model = Blog
        template_name = 'blog/detailedBlog.html'

class BlogCreateView(CreateView):
    model= Blog
    form_class= BlogPostForm
    template_name= 'blog/addBlog.html'
    #fields= '__all__'
    #fields= ('blogPostName',)
        