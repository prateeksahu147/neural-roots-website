from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from .models import Job
from .forms import JobPostForm
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
# Create your views here.
"""
def careers(request):
    jobs = Job.objects
    return render(request, 'careers/careers.html', {'jobs': jobs,})
"""
# class based views
# ListView gives list of all quaries
# DetailViews gives one set of query 
class CareerView(ListView):
    model = Job # assign model  what we use for this view
    template_name  = "careers/careers.html"
    paginate_by = 3  #and that's it !!
    
    def get_context_data(self, **kwargs):
        """
        this code for pagination
        https://stackoverflow.com/questions/5907575/how-do-i-use-pagination-with-django-class-based-generic-listviews
        source code
        """
        context = super(CareerView, self).get_context_data(**kwargs) 
        list_exam = Job.objects.all()
        paginator = Paginator(list_exam, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            file_exams = paginator.page(page)
        except PageNotAnInteger:
            file_exams = paginator.page(1)
        except EmptyPage:
            file_exams = paginator.page(paginator.num_pages)
            
        context['list_exams'] = file_exams
        return context
    

class JobDetailView(DetailView):
    model = Job
    template_name= "careers/jobDetails.html"

class JobPostView(CreateView):
    model = Job
    form_class= JobPostForm
    template_name = "careers/jobPost.html"
    #fields = '__all__'
    # if we don't want all fields thn do this
    #fields= ('jobName', 'jobType')
