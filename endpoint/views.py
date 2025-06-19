from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from endpoint.models import Device,Payload
from endpoint.serializers import DeviceSerializer,PayloadSerializer
from base64 import b64decode
from django.db.utils import IntegrityError
class DeviceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] #checking for token
    def create(self, request): # POST
        try:
            data = request.data
            devEUI = data['devEUI']
            Device.objects.create(devEUI=devEUI,status=False)
            return Response(status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({"error":"id already exists"},status=status.HTTP_409_CONFLICT)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    

class PayloadViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] #checking for token
    def create(self, request): # POST
        try:
            data = request.data
            fCnt = data["fCnt"] 
            devEUI = data["devEUI"]
            encoded_data = data["data"]
            #checking for duplicate playload, by fCnt and foreign key devEUI
            reused = Payload.objects.filter(fCnt = fCnt, device__devEUI=devEUI).exists()
            if reused:
                return Response(status = status.HTTP_409_CONFLICT)
            else:
                decoded = int.from_bytes(b64decode(encoded_data), 'big')
                payload_status = True if decoded == 1 else False
                device = Device.objects.get(devEUI = devEUI)
                device.status = payload_status
                Payload.objects.create(fCnt=fCnt,status=payload_status,device=device)
                device.save()
                return Response(status=status.HTTP_201_CREATED)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Device.DoesNotExist:
            return Response({"error":"invalid device id"},status=status.HTTP_400_BAD_REQUEST)
    # default behavior to show all payloads
    queryset = Payload.objects.all()
    serializer_class = PayloadSerializer
