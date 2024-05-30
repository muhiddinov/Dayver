from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IoTDeviceViewSet, IoTDataViewSet, dashboard

router = DefaultRouter()
router.register(r'devices', IoTDeviceViewSet)
router.register(r'data', IoTDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', dashboard, name='dashboard'),
]
