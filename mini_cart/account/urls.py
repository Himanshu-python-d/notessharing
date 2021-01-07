from .views import *
from django.urls import path, include

urlpatterns = [
    path('', login, name="login"),
    path('register', register, name="register"),
    path('otp', otp, name="otp")
]
