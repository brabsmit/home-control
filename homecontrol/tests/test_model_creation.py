import os.path
import unittest
import requests
import json

class DoorTestCase(unittest.TestCase):
   """Test case for the Door model creation methods."""

   def setUp(self):
      self.api_base = 'http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com'
      self.username = 'test-user'
      self.room_pk = 7
      self.door_creation_name = 'test_door_creation'
      self.door_patch_pk = 26
     
   def tearDown(self):
      url = self.api_base+'/api/door/'
      headers = {'content-type': 'application/json'}
      r = requests.get(url, headers=headers)
      response = json.loads(r.text)
      for door in response:
         if door['name'] == self.door_creation_name:
            url = self.api_base+'/api/door/'+str(door['pk'])+'/'
            r = requests.delete(url, headers = headers)
         elif door['pk'] == self.door_patch_pk:
            url = self.api_base+'/api/door/'+str(self.door_patch_pk)+'/'
            parameters = {
               'is_open': False,
               'is_locked': False,
            }
            r = requests.patch(url, data=json.dumps(parameters), headers = headers)
      
      
   def test_door_creation(self):
      """Test a simple door creation with defaults."""
      parameters = {
         'room': '/api/room/'+str(self.room_pk)+'/',
         'name': self.door_creation_name
      }
      url = self.api_base+'/api/door/'
      headers = {'content-type': 'application/json'}
      r = requests.post(url, data=json.dumps(parameters), headers=headers)
      status_code = r.status_code
      response = json.loads(r.text)
      
      self.assertEqual(status_code, 201)
      self.assertIsNotNone(response['pk'])
      self.assertEqual(response['is_locked'], False)
      self.assertEqual(response['is_open'], False)
      self.assertEqual(response['room'], self.api_base+'/api/room/'+str(self.room_pk)+'/')
      self.assertEqual(response['name'], self.door_creation_name)
   
   def test_door_patch(self):
      """Tweak a door's parameters and see if changes are reflected correctly"""
      parameters = {
         'is_locked': True,
         'is_open': True
      }
      url = self.api_base+'/api/door/'+str(self.door_patch_pk)+'/'
      headers = {'content-type': 'application/json'}
      r = requests.patch(url, data=json.dumps(parameters), headers=headers)
      status_code = r.status_code
      response = json.loads(r.text)
      
      self.assertEqual(status_code, 200)
      self.assertEqual(response['pk'], self.door_patch_pk)
      self.assertEqual(response['is_locked'], True)
      self.assertEqual(response['is_open'], True)
      self.assertEqual(response['room'], self.api_base+'/api/room/'+str(self.room_pk)+'/')
      self.assertIsNotNone(response['name'])
      
class LightTestCase(unittest.TestCase):
   """Test case for the Light model creation methods."""

   def setUp(self):
      self.api_base = 'http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com'
      self.username = 'test-user'
      self.room_pk = 7
      self.light_creation_name = 'test_light_creation'
      self.light_patch_pk = 8
     
   def tearDown(self):
      url = self.api_base+'/api/light/'
      headers = {'content-type': 'application/json'}
      r = requests.get(url, headers=headers)
      response = json.loads(r.text)
      for light in response:
         if light['name'] == self.light_creation_name:
            url = self.api_base+'/api/light/'+str(light['pk'])+'/'
            r = requests.delete(url, headers = headers)
         elif light['pk'] == self.light_patch_pk:
            url = self.api_base+'/api/light/'+str(self.light_patch_pk)+'/'
            parameters = {
               'is_on': False,
            }
            r = requests.patch(url, data=json.dumps(parameters), headers = headers)
      
      
   def test_light_creation(self):
      """Test a simple light creation with defaults."""
      parameters = {
         'room': '/api/room/'+str(self.room_pk)+'/',
         'name': self.light_creation_name
      }
      url = self.api_base+'/api/light/'
      headers = {'content-type': 'application/json'}
      r = requests.post(url, data=json.dumps(parameters), headers=headers)
      status_code = r.status_code
      response = json.loads(r.text)
      
      self.assertEqual(status_code, 201)
      self.assertIsNotNone(response['pk'])
      self.assertEqual(response['is_on'], False)
      self.assertEqual(response['room'], self.api_base+'/api/room/'+str(self.room_pk)+'/')
      self.assertEqual(response['name'], self.light_creation_name)
   
   def test_light_patch(self):
      """Tweak a light's parameters and see if changes are reflected correctly"""
      parameters = {
         'is_on': True
      }
      url = self.api_base+'/api/light/'+str(self.light_patch_pk)+'/'
      headers = {'content-type': 'application/json'}
      r = requests.patch(url, data=json.dumps(parameters), headers=headers)
      status_code = r.status_code
      response = json.loads(r.text)
      
      self.assertEqual(status_code, 200)
      self.assertEqual(response['pk'], self.light_patch_pk)
      self.assertEqual(response['is_on'], True)
      self.assertEqual(response['room'], self.api_base+'/api/room/'+str(self.room_pk)+'/')
      self.assertIsNotNone(response['name'])
 
class RefrigeratorTestCase(unittest.TestCase):
   """Test case for the refrigerator model creation methods."""

   def setUp(self):
      self.api_base = 'http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com'
      self.username = 'test-user'
      self.room_pk = 7
      self.refrigerator_creation_name = 'test_refrigerator_creation'
      self.refrigerator_patch_pk = 2
     
   def tearDown(self):
      url = self.api_base+'/api/refrigerator/'
      headers = {'content-type': 'application/json'}
      r = requests.get(url, headers=headers)
      response = json.loads(r.text)
      for refrigerator in response:
         if refrigerator['name'] == self.refrigerator_creation_name:
            url = self.api_base+'/api/refrigerator/'+str(refrigerator['pk'])+'/'
            r = requests.delete(url, headers = headers)
         elif refrigerator['pk'] == self.refrigerator_patch_pk:
            url = self.api_base+'/api/refrigerator/'+str(self.refrigerator_patch_pk)+'/'
            parameters = {
               'fridge_set_temp': 36,
               'fridge_current_temp': 35,
               'freezer_set_temp': 0,
               'freezer_current_temp': 1
            }
            r = requests.patch(url, data=json.dumps(parameters), headers = headers)
      
      
   def test_refrigerator_creation(self):
      """Test a simple refrigerator creation with defaults."""
      parameters = {
         'room': '/api/room/'+str(self.room_pk)+'/',
         'name': self.refrigerator_creation_name,
         'fridge_current_temp': 35,
         'freezer_current_temp': 1
      }
      url = self.api_base+'/api/refrigerator/'
      headers = {'content-type': 'application/json'}
      r = requests.post(url, data=json.dumps(parameters), headers=headers)
      status_code = r.status_code
      response = json.loads(r.text)
      
      self.assertEqual(status_code, 201)
      self.assertIsNotNone(response['pk'])
      self.assertEqual(response['fridge_set_temp'], 36)
      self.assertEqual(response['fridge_current_temp'], 35)
      self.assertEqual(response['freezer_set_temp'], 0)
      self.assertEqual(response['freezer_current_temp'], 1)
      self.assertEqual(response['room'], self.api_base+'/api/room/'+str(self.room_pk)+'/')
      self.assertEqual(response['name'], self.refrigerator_creation_name)
      
      self.refrigerator_pk = response['pk']
   
   def test_refrigerator_patch(self):
      """Tweak a refrigerator's parameters and see if changes are reflected correctly"""
      parameters = {
         'fridge_set_temp': 37,
         'fridge_current_temp': 36,
         'freezer_set_temp': 1,
         'freezer_current_temp': 2
      }
      url = self.api_base+'/api/refrigerator/'+str(self.refrigerator_patch_pk)+'/'
      headers = {'content-type': 'application/json'}
      r = requests.patch(url, data=json.dumps(parameters), headers=headers)
      status_code = r.status_code
      response = json.loads(r.text)
      
      self.assertEqual(status_code, 200)
      self.assertEqual(response['pk'], self.refrigerator_patch_pk)
      self.assertEqual(response['fridge_set_temp'], 37)
      self.assertEqual(response['fridge_current_temp'], 36)
      self.assertEqual(response['freezer_set_temp'], 1)
      self.assertEqual(response['freezer_current_temp'], 2)
      self.assertEqual(response['room'], self.api_base+'/api/room/'+str(self.room_pk)+'/')
      self.assertIsNotNone(response['name']) 
      
class ThermostatTestCase(unittest.TestCase):
   """Test case for the thermostat model creation methods."""

   def setUp(self):
      self.api_base = 'http://ec2-54-153-19-113.us-west-1.compute.amazonaws.com'
      self.username = 'test-user'
      self.room_pk = 7
      self.home_pk = 2
      self.thermostat_creation_name = 'test_thermostat_creation'
      self.thermostat_patch_pk = 4
     
   def tearDown(self):
      url = self.api_base+'/api/thermostat/'
      headers = {'content-type': 'application/json'}
      r = requests.get(url, headers=headers)
      response = json.loads(r.text)
      for thermostat in response:
         if thermostat['name'] == self.thermostat_creation_name:
            url = self.api_base+'/api/thermostat/'+str(thermostat['pk'])+'/'
            r = requests.delete(url, headers = headers)
         elif thermostat['pk'] == self.thermostat_patch_pk:
            url = self.api_base+'/api/thermostat/'+str(self.thermostat_patch_pk)+'/'
            parameters = {
               'current_temp': 72,
               'set_temp': 70
            }
            r = requests.patch(url, data=json.dumps(parameters), headers = headers)
      
      
   def test_thermostat_creation(self):
      """Test a simple thermostat creation with defaults."""
      parameters = {
         'home': '/api/home/'+str(self.home_pk)+'/',
         'name': self.thermostat_creation_name,
         'current_temp': 69,
         'set_temp': 68
      }
      url = self.api_base+'/api/thermostat/'
      headers = {'content-type': 'application/json'}
      r = requests.post(url, data=json.dumps(parameters), headers=headers)
      status_code = r.status_code
      response = json.loads(r.text)
      
      self.assertEqual(status_code, 201)
      self.assertIsNotNone(response['pk'])
      self.assertEqual(response['current_temp'], 69)
      self.assertEqual(response['set_temp'], 68)
      self.assertEqual(response['home'], self.api_base+'/api/home/'+str(self.home_pk)+'/')
      self.assertEqual(response['name'], self.thermostat_creation_name)
   
   def test_thermostat_patch(self):
      """Tweak a thermostat's parameters and see if changes are reflected correctly"""
      parameters = {
         'current_temp': 85,
         'set_temp': 80
      }
      url = self.api_base+'/api/thermostat/'+str(self.thermostat_patch_pk)+'/'
      headers = {'content-type': 'application/json'}
      r = requests.patch(url, data=json.dumps(parameters), headers=headers)
      status_code = r.status_code
      response = json.loads(r.text)
      
      self.assertEqual(status_code, 200)
      self.assertEqual(response['pk'], self.thermostat_patch_pk)
      self.assertEqual(response['current_temp'], 85)
      self.assertEqual(response['set_temp'], 80)
      self.assertEqual(response['home'], self.api_base+'/api/home/'+str(self.home_pk)+'/')
      self.assertIsNotNone(response['name'])
      