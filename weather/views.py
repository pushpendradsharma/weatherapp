from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import SearchForm, LoginForm, SignupForm
from .models import SearchData
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import auth
from django.conf import settings
import requests
from django import forms

# settings.ACCUWEATHER_API_KEY

def Dashboard(request):
    if request.user.is_authenticated:
        search_result = {}
        print("search_result: ", search_result)
        if 'city' in request.GET:
            form = SearchForm(request.GET)
            if form.is_valid():
                response = form.search()
                print("response: ", response)
                if isinstance(response, list) and response:
                    search_result = response[0]  # Considering response is a list, take the first item
                    print("search_result: ", search_result)
                    if isinstance(search_result, dict) and 'Key' in search_result:
                        key = search_result['Key']
                        print("key: ", key)
                        request.session['searched_key'] = key
        else:
            form = SearchForm()
    else:
        return HttpResponseRedirect('/login/')
    return render(request, 'index.html', {'form': form, 'search_result': search_result})

def SearchWeather(request):
    search_result = {}
    if 'city' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = SearchForm()
    return render(request, 'index.html', {'form': form, 'search_result': search_result})

def Signup(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm = SignupForm(request.POST)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/login/')
        else:
            fm = SignupForm()
        context = {'form':fm}
        return render(request, 'signup.html', context)
    else:
        return HttpResponseRedirect('/')

def Login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/')
        else:
            fm = LoginForm()
        context = {'form':fm}
        return render(request, 'login.html', context)
    else:
        return HttpResponseRedirect('/')

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')