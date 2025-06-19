from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from endpoint.models import Device,Payload
from endpoint.serializers import DeviceSerializer,PayloadSerializer
from base64 import b64decode

class DeviceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
class PayloadViewSet(viewsets.ModelViewSet):
    #checking for token
    permission_classes = [IsAuthenticated]
    def create(self, request): # Post request
        try:
            data = request.data
            fCnt = data["fCnt"] 
            devEUI = data["devEUI"]
            encoded_data = data["data"]
            reused = Payload.objects.filter(fCnt = fCnt, device__devEUI=devEUI).exists()
            if reused:
                return Response(status = status.HTTP_409_CONFLICT)
            else:
                decoded = int.from_bytes(b64decode(encoded_data), 'big')
                payload_status = True if decoded == 1 else False
                device = Device.objects.get(devEUI = devEUI)
                Payload.objects.create(fCnt=fCnt,status=payload_status,device=device)
            return Response(status=status.HTTP_202_ACCEPTED)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    queryset = Payload.objects.all()
    serializer_class = PayloadSerializer
