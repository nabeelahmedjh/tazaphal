from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
from dotenv import load_dotenv
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import time

# Create your views here.

load_dotenv()


def loginView(request):

    if request.method == "GET":
        ...

    elif request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')


def logoutView(request):
    logout(request)
    return HttpResponse("Logged out")


def registrationView(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return redirect('register')

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(
                username=username, password=password)
            user.save()
            return HttpResponse("User created")
        else:
            return HttpResponse("User already exists")

    return render(request, 'register.html')


def home(request):

    return render(request, 'index.html')


def contact(request):

    if request.method == 'POST':

        time.sleep(3)
        # return 200 status code
        return JsonResponse({'success': True})

    return render(request, 'contact.html')
