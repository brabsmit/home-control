from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from geoposition import Geoposition

# Create your views here.

def home(request):
   return render(request, 'index.html')

def register(request):
   if request.user.is_authenticated():
      return HttpResponseRedirect("/dashboard/")
   else:
      if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect("/dashboard/")
      else:
         form = UserCreationForm()
      return render(request, "register.html", {
         'form': form,
      })

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/dashboard/")
    else:
        form = AuthenticationForm()
    return render(request, "signin.html", {
        'form': form,
    })

def signout(request):
   logout(request)
   return HttpResponseRedirect("/signin/")

@login_required(login_url='/signin/')
def dashboard(request):
   return render(request, 'dashboard.html')
   