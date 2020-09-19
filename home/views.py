from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home/home.html')


def login(request):
    return render(request, 'home/default-login.html')


def signup(request):
    return render(request, 'home/default-register.html')

def calculator(request):
    return render(request, 'home/calculator.html')
