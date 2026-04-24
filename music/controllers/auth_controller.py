from django.shortcuts import render, redirect

def landing_page(request):
    return render(request, 'landing.html')

def login_page(request):
    return render(request, 'login.html')