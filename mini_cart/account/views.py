from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
import random


import http.client

from django.conf import settings
# Create your views here.

def send_otp(mobile , otp):
    conn = http.client.HTTPSConnection("api.msg91.com")
    authkey = settings.authkey
    headers = { 'content-type': "application/json" }
    url = "http://control.msg91.com/api/sendotp.php?otp="+otp+'&sender=ABC&message='+'Your otp is'+otp +'&mobile'+mobile+'&authkey='+authkey+'&country=91'
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    return None

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')

        check_user = User.objects.filter(email = email).first()
        check_profile = Profile.objects.filter(mobile = mobile).first()

        if check_user or check_profile:
            context = {'message': 'User already exist','class': 'danger'}
            return render(request,'register.html',context)

        user = User(email = email, first_name = name)
        user.save()

        otp = str(random.randint(1000, 9999))

        profile = Profile(user= user, mobile =mobile, otp=otp)
        profile.save()
        send_otp(mobile,otp)
        request.session['mobile'] = mobile
        return redirect('otp')
    return render(request, 'register.html')

def otp(request):
    mobile = request.session['mobile']
    context = {'mobile':mobile}
    return render(request, 'otp.html', context)
