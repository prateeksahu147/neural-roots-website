from django import forms
from .models import Job



class JobPostForm(forms.ModelForm):
    class Meta:
            model= Job
            fields= ('jobName', 'jobType','jobLocation','jobDescription','jobPublishedDate','jobVacancy')
            widgets= {
                'jobName': forms.TextInput(attrs={'class': 'form-control'}),
                'jobType': forms.TextInput(attrs={'class': 'form-control'}),
                'jobLocation': forms.TextInput(attrs={'class': 'form-control'}),
                'jobDescription': forms.Textarea(attrs={'class': 'form-control'}),
                #'jobPublishedDate': forms.DateTimeField({'class': 'form-control'}),
                #'jobVacancy': forms.IntegerField({'class': 'form-control'}),
            }