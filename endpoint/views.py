from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from endpoint.models import Device,Payload
from rest_framework.authtoken.models import Token
from endpoint.serializers import DeviceSerializer,PayloadSerializer
class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
class PayloadViewSet(viewsets.ModelViewSet):
    #checking for token
    permission_classes = [IsAuthenticated]
    def create(self, request):
        data = request.data
        fCnt = data["fCnt"]
        devEUI = data["devEUI"]
        reused = Payload.objects.filter(fCnt = fCnt).exists()
        if reused:
            return Response(status = status.HTTP_409_CONFLICT)
        else:
            device = Device.objects.get(devEUI=devEUI)
            Payload.objects.create(fCnt=fCnt,status=1,device=device)
        return Response(status=status.HTTP_202_ACCEPTED)
    queryset = Payload.objects.all()
    serializer_class = PayloadSerializer
