from django.shortcuts import render
from rest_framework import viewsets
from endpoint.models import Device,Payload
from endpoint.serializers import DeviceSerializer,PayloadSerializer
class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
class PayloadViewSet(viewsets.ModelViewSet):
    queryset = Payload.objects.all()