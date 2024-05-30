from rest_framework import viewsets
from .models import IoTDevice, IoTData
from .serializers import IoTDeviceSerializer, IoTDataSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

class IoTDeviceViewSet(viewsets.ModelViewSet):
    queryset = IoTDevice.objects.all()
    serializer_class = IoTDeviceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return IoTDevice.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class IoTDataViewSet(viewsets.ModelViewSet):
    queryset = IoTData.objects.all()
    serializer_class = IoTDataSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return IoTData.objects.filter(device__user=self.request.user)

def dashboard(request):
    iotdata = IoTData.objects.filter(device__user=request.user)
    return render(request, 'dayver/dashboard.html', {'iotdata': iotdata})