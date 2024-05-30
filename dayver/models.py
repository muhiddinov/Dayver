from django.contrib.auth.models import User
from django.db import models

class IoTDevice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=100)
    device_name = models.CharField(max_length=100)

    def __str__(self):
        return self.device_name

class IoTData(models.Model):
    device = models.ForeignKey(IoTDevice, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.device.device_name} - {self.timestamp}'
