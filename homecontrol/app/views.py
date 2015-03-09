from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from geoposition import Geoposition
from app.models import Home, Room, Light, Door, Refrigerator, Thermostat
from app.serializers import HomeSerializer, RoomSerializer, LightSerializer, DoorSerializer, RefrigeratorSerializer, ThermostatSerializer, UserSerializer

from rest_framework.response import Response
from rest_framework import viewsets

from django.db import IntegrityError

from sets import Set
import json

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
class HomeViewSet(viewsets.ModelViewSet):
   """
   API endpoint that allows homes to be viewed or edited.
   """
   queryset = Home.objects.all()
   serializer_class = HomeSerializer
   
class RoomViewSet(viewsets.ModelViewSet):
   """
   API endpoint that allows rooms to be viewed or edited.
   """
   queryset = Room.objects.all()
   serializer_class = RoomSerializer

class LightViewSet(viewsets.ModelViewSet):
   """
   API endpoint that allows lights to be viewed or edited.
   """
   queryset = Light.objects.all()
   serializer_class = LightSerializer

class DoorViewSet(viewsets.ModelViewSet):
   """
   API endpoint that allows doors to be viewed or edited.
   """
   queryset = Door.objects.all()
   serializer_class = DoorSerializer

class RefrigeratorViewSet(viewsets.ModelViewSet):
   """
   API endpoint that allows refrigerators to be viewed or edited.
   """
   queryset = Refrigerator.objects.all()
   serializer_class = RefrigeratorSerializer
   
class ThermostatViewSet(viewsets.ModelViewSet):
   """
   API endpoint that allows thermostats to be viewed or edited.
   """
   queryset = Thermostat.objects.all()
   serializer_class = ThermostatSerializer
   

# SettingsForm is an extension of an AuthenticationForm
class SettingsForm(forms.Form):
   # User settings
   new_username = forms.CharField(max_length=254,
                                  min_length=1,
                                  required=False,
                                  widget=forms.TextInput(attrs={
                                     'class' : 'form-control input-md'}))
   error_messages = {
     'password_mismatch': ("The two password fields didn't match."),
   }
   password1 = forms.CharField(label=("Password"),
      widget=forms.PasswordInput(attrs={'class' : 'form-control input-md'}),
      required=False)
   password2 = forms.CharField(label=("Password confirmation"),
      widget=forms.PasswordInput(attrs={'class' : 'form-control input-md'}),
      help_text=("Enter the same password as above, for verification."),
      required=False)

   def clean_password2(self):
      password1 = self.cleaned_data.get("password1")
      password2 = self.cleaned_data.get("password2")
      if password1 and password2 and password1 != password2:
         raise forms.ValidationError(self.error_messages['password_mismatch'])
      return password2

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
   context = {}
   if request.method == 'GET':
      user = User.objects.get(username=request.user)
      # get homes
      context['homes'] = Home.objects.filter(owner=user)
      context['rooms'] = {}
      context['lights'] = {}
      context['refrigerators'] = {}
      context['thermostats'] = {}
      context['doors'] = {}
      # get rooms
      for home in context['homes']:
         context['rooms'][home.pk] = Room.objects.filter(home=home)
         # get thermostats
         context['thermostats'][home.pk] = Thermostat.objects.filter(home=home)
         # get devices
         for room in context['rooms'][home.pk]:
            # get lights
            context['lights'][room.pk] = Light.objects.filter(room=room)
            # get refrigerators
            context['refrigerators'][room.pk] = Refrigerator.objects.filter(room=room)
            # get doors
            context['doors'][room.pk] = Door.objects.filter(room=room)
   return render(request, 'dashboard.html', context)

   
@login_required(login_url='/signin/')
def settings(request):
   context = {}
   user = request.user.id
   template = 'settings.html'
   if request.method == 'GET':
      if request.GET.get('account', False):
         form = SettingsForm()
         context['form'] = form
         user = User.objects.get(username=request.user)
         template = 'settings_account.html'
   return render(request, template, context)

   
@login_required(login_url='/signin/')
def settings_account(request):
  context = {}
  errors = Set()
  user = User.objects.get(username = request.user)
  if request.method == 'POST':
    context['success'] = False
    form = SettingsForm(request.POST)
    notifications = request.POST.getlist('notifications', False)
    context['notifications'] = []
    if notifications:
      # disassociate all notifications
      user.usersettings.notifications.clear()
      for notification in notifications:
         # associate chosen notifications
         context['notifications'].append(notification)
         n = Notification.objects.get(pk=notification)
         user.usersettings.notifications.add(n)
         user.save()
      context['success'] = True

    elif form.is_valid():
      user = User.objects.get(username = request.user)
      new_username = form.cleaned_data['new_username']
      password1 = form.cleaned_data['password1']
      password2 = form.cleaned_data['password2']
      notifications = request.POST.get('notifications')
      template = 'base/settings_account.html'

      if new_username:
        try:
          user.username = new_username
          user.save()
          context['success'] = True
          context['username'] = user.username
        except IntegrityError:
          errors.add("Username taken")

      if password1 and password2:
        try:
          form.clean_password2()
          user.set_password(password1)
          user.save()
          auth_user = authenticate(username=request.user, password=password1)
          if user is not None:
            login(request, auth_user)
          context['success'] = True
        except forms.ValidationError, e:
          errors.add('; '.join(e.messages))
    
    context['errors'] = list(errors)
    return HttpResponse(json.dumps(context), content_type="application/json")
  else: return render(request, 'settings.html')
