from django.contrib import admin
from app.models import Home, Room, Thermostat, Door, Light, Refrigerator

"""
Administrator interface customization

This module contains customization classes to the admin interface
rendered by Django. This file is interpreted at run time to serve
the custom administrator actions that correspond to the application's
custom models.
"""


class ThermostatAdmin(admin.ModelAdmin):
   """
   ModelAdmin
   """
   list_display = ('name','home','current_temp','set_temp','pk')
   search_fields = ('name','home')

class ThermostatInline(admin.StackedInline):
   """
   StackedInline
   """
   model = Thermostat

   
class DoorAdmin(admin.ModelAdmin):
   """
   ModelAdmin
   """
   list_display = ('name','room','is_locked','is_open','pk')
   search_fields = ('name','room')

class DoorInline(admin.StackedInline):
   """
   StackedInline
   """
   model = Door

   
class LightAdmin(admin.ModelAdmin):
   """
   ModelAdmin
   """
   list_display = ('name','room','is_on','pk')
   search_fields = ('name','room')

class LightInline(admin.StackedInline):
   """
   StackedInline
   """
   model = Light


class RefrigeratorAdmin(admin.ModelAdmin):
   """
   ModelAdmin
   """
   list_display = ('name','room','fridge_set_temp','fridge_current_temp','freezer_set_temp','freezer_current_temp','pk')
   search_fields = ('name','room')

class RefrigeratorInline(admin.StackedInline):
   """
   StackedInline
   """
   model = Refrigerator
   
   
class RoomAdmin(admin.ModelAdmin):
   """
   ModelAdmin
   """
   list_display = ('name','home','room_type','pk')
   search_fields = ('name','home')
   inlines = (DoorInline, LightInline, RefrigeratorInline,)

class RoomInline(admin.StackedInline):
   """
   StackedInline
   """
   model = Room


class HomeAdmin(admin.ModelAdmin):
   list_display = ('name','owner','position','secret_key','pk')
   search_fields = ('name',)
   readonly_fields=('secret_key',)
   inlines = (ThermostatInline, RoomInline, )


admin.site.register(Home, HomeAdmin)
admin.site.register(Thermostat, ThermostatAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Door, DoorAdmin)
admin.site.register(Light, LightAdmin)
admin.site.register(Refrigerator, RefrigeratorAdmin)
