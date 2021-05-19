from django.contrib import admin
from .models import Musician, Team, Contact, FAQ, Service

# Register your models here.

admin.site.register(Musician)
admin.site.register(Team)
admin.site.register(Service)
admin.site.register(FAQ)
admin.site.register(Contact)