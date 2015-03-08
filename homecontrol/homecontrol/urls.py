from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
   url(r'^admin/', include(admin.site.urls)),
   url(r'^docs/', include('rest_framework_swagger.urls')),
   url(r'^$', 'app.views.home', name='home'),
   url(r'^signin/$', 'app.views.signin'),
   url(r'^signout/$', 'app.views.signout'),
   url(r'^register/$', 'app.views.register'),
   url(r'^dashboard/$', 'app.views.dashboard'),
   url(r'^settings/$', 'app.views.settings'),
   url(r'^settings/account/$', 'app.views.settings_account'),
)
