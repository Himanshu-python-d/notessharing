from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import *

def show_about_page(request):
    print('About Page')
    name= 'Himanshu Aydav'
    return render(request,'about.html',{'name':name})

def show_home_page(request):
    cats = Category.objects.all()
    images = Image.objects.all()
    return render(request,'home.html',{'images':images,'cats':cats})

def show_category_page(request, cid):
    cats = Category.objects.all()
    category = Category.objects.get(pk=cid)
    images = Image.objects.filter(cat=category)
    return render(request,'home.html',{'images':images,'cats':cats})
