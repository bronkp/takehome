from endpoint.models import Device, Payload
from rest_framework import serializers

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ['devEUI', 'status']
class PayloadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payload
        fields = ['fCnt','status']