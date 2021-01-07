from django.contrib import admin
from .models import Contact,Contact1
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','message']

class Contact1Admin(admin.ModelAdmin):
    list_display=['name','email','message']

admin.site.register(Contact,ContactAdmin)
admin.site.register(Contact1,Contact1Admin)
