# Each app should have a “serializers.py” file (created manually)
# In this file we define serializer classes for each model in that same app
# The serializer class is responsible for converting JSON objects into the model type as well as converting objects into JSON


from rest_framework import serializers
from .models import Super

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'secondary_ability', 'catchphrase', 'super_type']
        #depth = 1
        #super_type_id = serializers.IntegerField(write_only=True) per powerpoint
