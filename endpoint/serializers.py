from endpoint.models import Device, Payload
from rest_framework import serializers

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ['devEUI', 'status']
class PayloadSerializer(serializers.HyperlinkedModelSerializer):
    #getting device id from foreign key
    device = serializers.SlugRelatedField(
        read_only=True,
        slug_field='devEUI'
     )
    class Meta:
        model = Payload
        fields = ('device','fCnt','status')