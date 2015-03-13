Specifications
==============

This project aims to provide a proof-of concept for the final project in
Computer Networking, CMPE 150, at the University of California, Santa Cruz. 
In this project, the aim was to explore the following:

[1] HOME CONTROL PROTOCOL: Design and specify a reliable IP­-based protocol to control
(check and manipulate state) some IP­-enabled devices (stereo, tv, vcr, lamps, heater) in your
home from remote, so that you can go on vacation and need not worry about whether you
switched off the lights. This protocol should be accessible from a webpage or app and allow
you to configure your home devices with timers.

In this project, the following specifications were achieved:

* IP-based protocol built on the `Django REST Framework <http://www.django-rest-framework.org/>`_

* Generic API endpoints for devices to check/manipulate own state
  (`Source <http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/docs/>`_) with support
  for the following devices:

  * Light
  	* Toggle on/off
  * Refrigerator
  	* View/Set fridge & freezer temperature
  * Thermostat
  	* View/Set thermostat temperature
  * Door
  	* View door open/closed
  	* View/Toggle door locked/unlocked

 * Website dashboard control of devices linked to user

 	* Homes and everything in them restricted to owner only

 	* Administrative interface to create models for the user

 	* Switch between different homes the user may own

RESTful API
===========

The API was built with flexibility and expandability in mind. Since the server was
created before the devices, the API specificaitons were made general enough such that
any device following the specification would be compatible. The API was also
exstensibly documented via `Swagger UI <http://swagger.io/>`_. The API has the
following controls:

* Home

  * `Create new home <http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/docs/#!/home/Home>`_

  * `Delete existing home <http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/docs/#!/home/Home_0_1_2_3_4>`_

* Room

  * `Create new room <http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/docs/#!/room/Room>`_

  * `Delete existing room <http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/docs/#!/room/Room_0_1_2_3_4>`_

* Thermostat

  * `Create new thermostat <http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/docs/#!/thermostat/Thermostat>`_

  * `Modify existing thermostat <http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/docs/#!/thermostat/Thermostat_0_1_2_3>`_

  * `Delete existing thermostat <http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/docs/#!/thermostat/Thermostat_0_1_2_3_4>`_

* Door

  * `Create new door <http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/docs/#!/door/Door>`_

  * `Modify existing door <http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/docs/#!/door/Door_0_1_2_3>`_

  * `Remove existing door <http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/docs/#!/door/Door_0_1_2_3_4>`_

* Light

  * `Create new light <http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/docs/#!/light/Light>`_

  * `Modify existing light <http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/docs/#!/light/Light_0_1_2_3>`_

  * `Remove existing light <http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/docs/#!/light/Light_0_1_2_3_4>`_

* Refrigerator

  * `Create new refrigerator <http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/docs/#!/refrigerator/Refrigerator>`_

  * `Modify existing refrigerator <http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/docs/#!/refrigerator/Refrigerator_0_1_2_3>`_

  * `Remove existing refrigerator <http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/docs/#!/refrigerator/Refrigerator_0_1_2_3_4>`_

The system is designed such that the devices should be able to self register, storing the primary key
value that links it to the database. This is the value the devices uses to reference itself when
making a mnodification. Example software flow:

.. code-block:: guess

	# Sample code for a light to register itself in system. Assumes the
	# light knows which room it belongs to.

	# POST to /lights/ endpoint, creating a new light in the database
	curl -X POST \
	-H "Content-Type: application/json" \
	-d '{"room":"/api/room/1/", "name": "New Light"}' \
	http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/api/light/
	
	# The following is then returned by the server.
	# The light must take note of the pk, which is used in the future.
	{"room":"http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/api/room/1/","name":"New Light","is_on":false,"pk":34}


With the device registered with the system, it now has access to an endpoint to modify its current state:

.. code-block:: guess

	# Sample code for a light to modify its state.

	# PATCH to /lights/pk/ where pk was given at creation
	curl -X PATCH \
	-H "Content-Type: application/json" \
	-d '{"is_on", "true"}' \
	http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/api/light/34/


You can use this as a crude way to verify that devices can be created/modified as per the requisite.


Database Schema
===============

The devices in this application were designed to have a nested relationship as follows:

User -> Home -> Room -> Device

If we were given the pk to a device, we could traverse the tree back up to get all pertinent
information about its location, context, and owner. The database has the following graph:

.. image:: http://i.imgur.com/VGWMbRV.png?1

A typical User model would have the following attributes:

.. code-block:: guess
	
	User {
		Home {
			Thermostat,
			Room {
				Light,
				Door,
				...
			},
			Room {
				Light,
				Refrigerator,
				...
			},
			...
		},
		...
	}

As you can see, a user can have multiple homes. Within those homes, there can be
any number of rooms with any combination of devices that describe the room.


Administrative Server Interfacing
=================================

With the ability to create and modify devices exposed to the world, there needs
to be a way to link those devices with a user model accessible via a web
application. Since this is a proof-of-concept, the management of resources
on the server side is limited to an administrator interface. This is not
production-worthy, but is an excellent tool to prove that things work.

The `Administrator Interface <http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/admin/>`_
is available to the "instructor" user (don't tell anyone, but the password is "networking").

Once logged in, the admin is presented with all the models that can be
modified. Currently, there are three homes, two that belong to the instructor
and one that belongs to a test user (explained later). Clicking on a home will
bring up that specific home's first-layer settings, such as its location, name, owner,
and thermostat.

From this interface, models can be added and linked. Any changes made in this interface
will be reflected on the dashboard for the user being changed.


User Dashboard
==============

`Live Demo <http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com/dashboard/>`_

(Log in as instructor with credentials provided above)

The dashboard was bult with responsiveness as the first priority. In Django's
web model, requests are served by rendering templates with context. Context is
a python dictionary defined at run-time of various variables pertinent to 
the creation of the page content. For example, the dashboard has a table with
a list of homes. This table has the following html:

.. code-block:: html

	<ul>
	{% for home in homes %}
		<li> {{ home.name }} </li>
	{% endfor %}
	</ul>

As you can see, this is clearly not pure html. The brackets signify
a Django qualifier that is rendered as the page is loaded. On the server
side, there is code to populate an array of homes for translation:

.. code-block:: python
	
	def dashboard(request):
		context = {}
		homes = Home.objects.get(owner=request.user)
		# Assuming an array of Device objects has been instantiated
		for home in homes:
			context['homes'].append(home)
		return render(request, 'dashboard.html', context)

The HTML served to the client will resemble something like this:

.. code-block:: html

	<ul>
		<li> My Home </li>
		<li> Vacation Home </li>
	</ul>

After the page is loaded, there are many buttons and sliders that
are created. These correspond to actions that modify the state
of the devices specified on the page. For instance, lights have
a button that is green when the light is on, and red when the 
light is off. If the user clicks the button, a jQuery AJAX request
is made to the server which toggles the state of the light. If the
toggle was successful, the button will toggle its color.

This method is true for all actions on the page, including the slider.



