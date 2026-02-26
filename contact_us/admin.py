from django.contrib import admin

from doctor import models
from .models import Contactus
# Register your models here.
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','phone','Problem']
admin.site.register(Contactus,ContactModelAdmin)