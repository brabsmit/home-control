from app.models import Home
from rest_framework import serializers

class HomeSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
      model = Home
      fields = ('owner', 'secret_key', 'serial', 'name')