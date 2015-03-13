=====
Homecontrol
=====

***[LIVE DEMO](http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/)***

***[Full Documentation](http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/documentation/)***

Sandbox user credentials:
username: home
password: control

Homecontrol is a simple Django app that provides proof-of-concept
for the generic control of any number of internet-connected homes.

A generic REST API is exposed to devices in a home that are to be
controlled and/or viewed by a user via a dashboard. Device
state and control information are stored in a sqlite3 database
and retrieved via AJAX for the user to view/manipulate.

The API itself is documented [here](http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/).
From this interface, you can play around with adding, modifying, and deleting 
(not recommended) devices, homes, and rooms.

Detailed documentation is in the "docs" directory.

Quick start
-----------

If you'd rather install the package yourself and run it via a new instance
of Django, follow these steps:

Required packages:
  rest_framework,
  rest_framework_swagger,
  geoposition,
  ws4redis

1. Add "homecontrol_app" to your INSTALLED_APPS setting like this::

	```python
    INSTALLED_APPS = (
        ...
        'homecontrol_app',
    )
    ```

2. Register the following to a DefaultRouter in your project urls.py like this:

	```python
	router.register(r'home', homecontrol_app.views.HomeViewSet)
	router.register(r'room', homecontrol_app.views.RoomViewSet)
	router.register(r'light', homecontrol_app.views.LightViewSet)
	router.register(r'refrigerator', homecontrol_app.views.RefrigeratorViewSet)
	router.register(r'thermostat', homecontrol_app.views.ThermostatViewSet)
	router.register(r'door', homecontrol_app.views.DoorViewSet)
	router.register(r'user', homecontrol_app.views.UserViewSet)
	```

3. Include the following URLconf in your project urls.py like this::

   ```python
   url(r'^admin/', include(admin.site.urls)),
   url(r'^docs/', include('rest_framework_swagger.urls')),
   url(r'^$', 'homecontrol_app.views.home', name='home'),
   url(r'^signin/$', 'homecontrol_app.views.signin'),
   url(r'^signout/$', 'homecontrol_app.views.signout'),
   url(r'^register/$', 'homecontrol_app.views.register'),
   url(r'^dashboard/$', 'homecontrol_app.views.dashboard'),
   url(r'^dashboard/refresh/$', 'homecontrol_app.views.dashboard_refresh'),
   url(r'^settings/$', 'homecontrol_app.views.settings'),
   url(r'^settings/account/$', 'homecontrol_app.views.settings_account'),
   url(r'^api/', include(router.urls))
   ```

4. Run `python manage.py migrate` to create the homecontrol models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a home (you'll need the Admin app enabled).

6. From admin, populate a home with rooms and devices that are expected
   to be connected.

5. Visit http://127.0.0.1:8000/ to view the dashboard.
