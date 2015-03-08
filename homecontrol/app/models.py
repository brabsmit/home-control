from django.db import models
from django.conf import settings
from geoposition.fields import GeopositionField

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
   
   ## used as the primary key for the model
   serial = models.IntegerField(unique=True, primary_key=True)
   
   ## name of house supplied by the user.
   name = models.CharField(max_length=30, blank=True, null=True)
   
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
      super(Device, self).save()      
