from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from App_login.forms import *

# Create your views here.


def signup_sys(request):
    form = UserSignUpForm()
    if request.method == 'POST':
        form = UserSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            this_user = form.save()
            return HttpResponseRedirect(reverse('App_login:login'))
    content = {'form': form}
    return render(request, 'App_login/signup.html', context=content)


def login_sys(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_main:home'))
    diction = {'form': form}
    return render(request, 'App_login/login.html', context=diction)


def logout_sys(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_login:login'))


