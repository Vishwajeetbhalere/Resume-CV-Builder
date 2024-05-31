from django.shortcuts import render, HttpResponse, redirect
from django.urls import path
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login


def index(request):
    # return HttpResponse('Hello World!')
    return render(request, 'core/index.html')


def loginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invaild Username or Password')
            return redirect('login')
    return render(request, 'core/login.html')


def dashboard(request):
    return render(request, 'core/dashboard.html')
