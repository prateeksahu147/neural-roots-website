from django.shortcuts import render
from .models import Team, Service, FAQ, Contact
# Create your views here.

def teamMembers(request):
    allMembers = Team.objects
    allServices = Service.objects
    allFAQs= FAQ.objects
    allContacts = Contact.objects
    return render(request, 'home/index.html', {'allMembers': allMembers, 'allServices': allServices,
                                                'allFAQs': allFAQs, 'allContacts': allContacts})

from django.core.mail import send_mail
def askInformation(request):
    if request.method == "POST":
        messageName= request.POST["name"]
        messageEmail=request.POST["email"]
        message =request.POST["message"]
        messageSubject = request.POST["subject"]


        send_mail(
                    messageSubject,
                    message,
                    messageEmail,
                    ['rootsneural@gmail.com'],
                    fail_silently=False,
                )

        print(message,messageEmail,)
        return render(request, 'home/index.html', {'message':message, 'messageEmail':messageEmail,
                                     'messageName':messageName, 'messageSubject':messageSubject})
    else: 
        print('chutiya')
        return render(request, 'home/index.html')
