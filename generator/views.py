from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))
    length = int(request.GET.get('length', 9))
    thepw = ''
    for x in range(length):
        thepw += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepw})

def about(request):
    return render(request, 'generator/about.html')
