from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Heyy !</h2>")
