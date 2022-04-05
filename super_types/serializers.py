# Each app should have a “serializers.py” file (created manually)
# In this file we define serializer classes for each model in that same app
# The serializer class is responsible for converting JSON objects into the model type as well as converting objects into JSON

from rest_framework import serializers
from .models import SuperType

class SuperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['type']