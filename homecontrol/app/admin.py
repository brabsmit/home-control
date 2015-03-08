from django.contrib import admin
from app.models import Home, Room, Thermostat, Door, Light, Refrigerator

"""@package(docstring)
Administrator interface customization

This module contains customization classes to the admin interface
rendered by Django. This file is interpreted at run time to serve
the custom administrator actions that correspond to the application's
custom models.
"""


class ThermostatAdmin(admin.ModelAdmin):
   list_display = ('name','home','current_temp','set_temp')
   search_fields = ('name','home')

class ThermostatInline(admin.StackedInline):
   model = Thermostat

   
class DoorAdmin(admin.ModelAdmin):
   list_display = ('name','room','is_locked','is_open')
   search_fields = ('name','room')

class DoorInline(admin.StackedInline):
   model = Door

   
class LightAdmin(admin.ModelAdmin):
   list_display = ('name','room','switch_mode','is_on')
   search_fields = ('name','room')

class LightInline(admin.StackedInline):
   model = Light


class RefrigeratorAdmin(admin.ModelAdmin):
   list_display = ('name','room','fridge_set_temp','fridge_current_temp','freezer_set_temp','freezer_current_temp',)
   search_fields = ('name','room')

class RefrigeratorInline(admin.StackedInline):
   model = Refrigerator
   
   
class RoomAdmin(admin.ModelAdmin):
   list_display = ('home','name','room_type',)
   search_fields = ('name','home')
   inlines = (DoorInline, LightInline, RefrigeratorInline,)

class RoomInline(admin.StackedInline):
   model = Room


class HomeAdmin(admin.ModelAdmin):
   list_display = ('name','owner','position','secret_key',)
   search_fields = ('name',)
   readonly_fields=('secret_key',)
   inlines = (ThermostatInline, RoomInline, )


admin.site.register(Home, HomeAdmin)
admin.site.register(Thermostat, ThermostatAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Door, DoorAdmin)
admin.site.register(Light, LightAdmin)
admin.site.register(Refrigerator, RefrigeratorAdmin)
