from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'aboutme/home.html')

def contact(request):
    return render(request, 'aboutme/contact.html', {'content': ['If you want to contact me, email at ','akshay.verma1115@gmail.com'] })

def register(request):
    return render(request, 'aboutme/register.html')
