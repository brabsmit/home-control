from app.models import Home, Room, Light, Door, Refrigerator, Thermostat
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
      model = User
      fields = ('username',)

class HomeSerializer(serializers.HyperlinkedModelSerializer):
   owner = UserSerializer(read_only=True)
   class Meta:
      model = Home
      fields = ('owner', 'name')

class RoomSerializer(serializers.HyperlinkedModelSerializer):
   home = HomeSerializer(read_only=True)
   class Meta:
      model = Room
      fields = ('home', 'name', 'room_type')

class LightSerializer(serializers.HyperlinkedModelSerializer):
   room = RoomSerializer(read_only=True)
   class Meta:
      model = Light
      fields = ('room', 'name', 'switch_mode', 'is_on','pk')
      
class DoorSerializer(serializers.HyperlinkedModelSerializer):
   room = RoomSerializer(read_only=True)
   class Meta:
      model = Door
      fields = ('room', 'name', 'is_locked','pk')

class RefrigeratorSerializer(serializers.HyperlinkedModelSerializer):
   room = RoomSerializer(read_only=True)
   class Meta:
      model = Refrigerator
      fields = ('room', 'name', 'fridge_set_temp','fridge_current_temp','freezer_set_temp','freezer_current_temp','pk')
      
class ThermostatSerializer(serializers.HyperlinkedModelSerializer):
   home = HomeSerializer(read_only=True)
   class Meta:
      model = Thermostat
      fields = ('home', 'name', 'controls','current_temp','set_temp','pk')