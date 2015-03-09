from app.models import Home, Room, Light, Door, Refrigerator, Thermostat
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
      model = User
      fields = ('username','pk')

class HomeSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
      model = Home
      fields = ('owner', 'name')

class RoomSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
      model = Room
      fields = ('home', 'name', 'room_type')

class LightSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
      model = Light
      fields = ('room', 'name', 'is_on','pk')
      
class DoorSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
      model = Door
      fields = ('room', 'name', 'is_locked','is_open','pk')

class RefrigeratorSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
      model = Refrigerator
      fields = ('room', 'name', 'fridge_set_temp','fridge_current_temp','freezer_set_temp','freezer_current_temp','pk')
      
class ThermostatSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
      model = Thermostat
      fields = ('home', 'name','current_temp','set_temp','pk')