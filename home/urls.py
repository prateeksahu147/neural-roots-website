from django.urls import path, include
from .views import askInformation, teamMembers

urlpatterns = [
    path('', teamMembers, name = 'home'),
    path('sent/', askInformation, name='sub'),
    
    
]