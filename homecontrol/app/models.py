from django.db import models
from django.conf import settings
from geoposition.fields import GeopositionField
from app import snippets
from django.forms import ModelForm

import string
import random

"""@package docstring
Model definitions.

This module contains the definitions for the various models used in this
application. These definitions are interpreted by Django and converted
into a sqlite database schema.
"""
   

class Home(models.Model):
   """Home model. Includes all devices that can be controlled.
   
   This model contains the relationships between the different
   types of devices that can be controlled in the app. Each house is
   instantiated uniquely. A house can have an owner.
   """
   
   ## owner attribute linked through the default Django user model
   owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
   
   ## key string used to pair a house with a user.
   secret_key = models.CharField(max_length=7, blank=True, null=True, editable=False)
   
   ## name of house supplied by the user.
   name = models.CharField(max_length=30)
   
   ## django-geoposition field for specifying house location
   position = GeopositionField(blank=True, null=True)
   
   def save(self, **kwargs):
      """ Custom save method to create random secret key"""
      if self.secret_key == None:
         ## 3 numerical digits
         secret_key =  ''.join(random.choice(string.digits) for i in range(3))
         ## 4 alphabetical characters
         secret_key += ''.join(random.choice(string.ascii_uppercase) for i in range(4))
         self.secret_key = secret_key
      super(Home, self).save()
      
   def __unicode__(self):
      return self.owner.username + ": " + self.name

      
class Room(models.Model):
   """Room model.
   
   Abstraction of a group of devices grouped into a single class.
   User can specify a name for a room and define actions based on room
   type. Many rooms per home.
   """
   
   ## foreign key linking a room to its home
   home = models.ForeignKey(Home)
   
   ## name of home supplied by the user.
   name = models.CharField(max_length=30)
   
   BEDROOM = 'BD'
   LIVING_ROOM = 'LR'
   KITCHEN = 'KT'
   BATHROOM = 'BR'
   HALLWAY = 'HW'
   DINING_ROOM = 'DR'
   PORCH = 'PR'
   PATIO = 'PT'
   OTHER = 'OT'
   ROOM_TYPES = (
      (BEDROOM, 'Bedroom'),
      (LIVING_ROOM, 'Living Room'),
      (KITCHEN, 'Kitchen'),
      (BATHROOM, 'Bathroom'),
      (HALLWAY, 'Hallway'),
      (DINING_ROOM, 'Dining Room'),
      (PORCH, 'Porch'),
      (PATIO, 'Patio'),
      (OTHER, 'Other'),
   )
   
   ## operation mode. Either binary or variable load.
   room_type = models.CharField(max_length=9,
      choices = ROOM_TYPES,
                                       default=OTHER)
   
   def __unicode__(self):
      return self.name + "\t(" + self.home.owner.username + ": " + self.home.name + ")"
   
      
class Light(models.Model):
   """Light model.
   
   This model contains the specifications for the type of light
   the user would like to add. Defaults to binary mode. Many lights per
   room.
   """
   ## foreign key linking a light to its room in a home
   room = models.ForeignKey(Room)
   
   ## name of the light supplied by the user.
   name = models.CharField(max_length=30, default='Light')
   
   BINARY = 'BN'
   VARIABLE = 'VB'
   SWITCH_MODE_CHIOICES = (
      (BINARY, 'On/Off'),
      (VARIABLE, 'Variable'),
   )
   
   ## operation mode. Either binary or variable load.
   switch_mode = models.CharField(max_length=2,
      choices = SWITCH_MODE_CHIOICES,
                                       default=BINARY)
                                       

class Refrigerator(models.Model):
   """Refrigerator model.
   
   This model exposes the refrigerator to the home control. It is
   designed to read and write fridge/freezer temperature.
   """
   
   ## foreign key linking a light to its room in a home
   room = models.ForeignKey(Room)
   
   ## name of the light supplied by the user.
   name = models.CharField(max_length=30, default='Refrigerator')
   
   ## thermostat temperature of refrigeration chamber
   fridge_set_temp = models.IntegerField(default=36)
   
   ## temperature reading of refrigeration chamber
   fridge_current_temp = models.IntegerField()
   
   ## thermostat temperature of freezer chamber
   freezer_set_temp = models.IntegerField(default=36)
   
   ## temperature reading of freezer chamber
   freezer_current_temp = models.IntegerField()
                                       
                                       
class Thermostat(models.Model):
   """Nest-like thermostat model.
   
   This model is designed to act like a Nest thermostat in the home.
   Its main purpose is to report and set thermostat temperature. One
   thermostat per home. User specifies if thermostat controls
   AC and/or heater.
   """
   
   ## foreign key linking a room to its home
   home = models.ForeignKey(Home)
   
   ## name of the light supplied by the user.
   name = models.CharField(max_length=30, default='Thermostat')
   
   AIR_CONDITION = 'AC'
   HEATER = 'HT'
   FAN = 'FN'
   CONTROL_CHOICES = (
      (AIR_CONDITION, 'Air Conditioner'),
      (HEATER, 'Heater'),
      (FAN, 'Fan'),
   )
   
   ## operation mode. Either binary or variable load.
   controls = snippets.MultiSelectField(max_length=3,
      choices = CONTROL_CHOICES)
   

class Door(models.Model):
   """Door model.
   
   This model contains the specifications for a door that leads
   into a room. Main goal of this model is to give controls to
   lock/unlock the door itself.
   """
   ## foreign key linking a light to its room in a home
   room = models.ForeignKey(Room)
   
   ## name of the light supplied by the user.
   name = models.CharField(max_length=30, default='Door')
   
   ## boolean field specifying if a door is locked or unlocked.
   locked = models.BooleanField(default=False)
   
   
   
   