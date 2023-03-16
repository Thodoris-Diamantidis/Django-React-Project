"""
Serializers allow complex data such as querysets and model instances
to be converted to native Python datatypes that can then be easily rendered 
into JSON, XML or other content types. Serializers also provide deserialization,
 allowing parsed data to be converted back into complex types, after first
validating the incoming data.
"""
from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    #Class meta is used to specify metadata about the serializer and the model it will serialize
    class Meta:
        #Specifies that the serializer should be used for the `Room` model
        model = Room
        #Specifies which fields of `Room` should be serialized
        fields = ('id', 'code', 'host', 'guest_can_pause',
                   'votes_to_skip', 'created_at')