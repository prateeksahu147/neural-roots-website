from django.db import models

# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Service(models.Model):
    serviceName =models.CharField(max_length=50)
    ServiceInfo =models.TextField()
    ServiceIcon =models.ImageField(upload_to= "media/home/service")
    def __str__(self):
        return self.serviceName ## by this function we can see our objects as title name in admin

class Team(models.Model):
    memberName =models.CharField(max_length=50)
    memberPhoto = models.ImageField(upload_to= "media/home/team")
    memberPost =models.CharField(max_length=50)
    abourMember =models.TextField(max_length = 500)
    memberInstagram =models.CharField(max_length=250)
    memberFacebook =models.CharField(max_length=250)
    memberLinkedIn =models.CharField(max_length=250)
    memberTwitter = models.CharField(max_length=250)

    def __str__(self):
        return self.memberName ## by this function we can see our objects as title name in admin


class FAQ(models.Model):
    questionNumber= models.IntegerField()
    question =models.TextField()
    answer =models.TextField()


class Contact(models.Model):
    location =models.TextField()
    email = models.EmailField(max_length=50)  
    phone = models.IntegerField() 
