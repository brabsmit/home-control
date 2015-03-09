from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from app import views


router = routers.DefaultRouter()
router.register(r'home', views.HomeViewSet)
router.register(r'room', views.RoomViewSet)
router.register(r'light', views.LightViewSet)
router.register(r'refrigerator', views.RefrigeratorViewSet)
router.register(r'thermostat', views.ThermostatViewSet)
router.register(r'door', views.DoorViewSet)
router.register(r'user', views.UserViewSet)


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
   
   url(r'^api/', include(router.urls)),
)
