from django.urls import path, include
from .views import CareerView, JobDetailView, JobPostView
#import all class from views

urlpatterns = [
    #path('', views.careers, name = 'careers'),
    path('', CareerView.as_view(), name= 'career'),
    # "as_view() id method for access view class "
    path('job/<int:pk>', JobDetailView.as_view(), name = 'job' ),
    path('jobPost',JobPostView.as_view() , name= 'jobPost'),
]