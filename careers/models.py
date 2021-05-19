from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.


class InfoM(models.Model):
    name= models.CharField(max_length= 50)
    def __str__(self):
        return self.name


class Job(models.Model):
    jobName =models.CharField(max_length = 50)
    jobType =models.CharField(max_length = 50)
    jobLocation =models.CharField(max_length = 50)
    jobDescription =RichTextField(blank= True, null= True)
    jobPublishedDate =models.DateTimeField()
    jobVacancy =models.IntegerField()

    def __str__(self):
        return self.jobName

    def get_absolute_url(self):
        """
        this method take back whereever we want to go
        reverse() method take 1st argument "name" of urlspattern fro, urls.py  
        """
        #return reverse('job', args= (str(self.id)))
        return reverse("career")
