from django.contrib import admin
from app.models import Home

"""@package(docstring)
Administrator interface customization

This module contains customization classes to the admin interface
rendered by Django. This file is interpreted at run time to serve
the custom administrator actions that correspond to the application's
custom models.
"""

class HomeAdmin(admin.ModelAdmin):
   list_display = ('name','owner','serial','position','secret_key',)
   search_fields = ('name','serial')
   readonly_fields=('secret_key',)

admin.site.register(Home, HomeAdmin)