from rest_framework import serializers
from .models import IoTDevice, IoTData

class IoTDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IoTDevice
        fields = '__all__'

class IoTDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = IoTData
        fields = '__all__'
