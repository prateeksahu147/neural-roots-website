from .views import BlogListView, BlogDetailView, BlogCreateView, viewCategoryPost
from django.urls import path, include

urlpatterns = [

    path('', BlogListView.as_view(), name='blog'),
    path('addBlog', BlogCreateView.as_view(), name='add-blog'),
    path('<int:pk>', BlogDetailView.as_view(), name= 'read'),
    path('<str:cats>', viewCategoryPost, name='catigory-post'),

]