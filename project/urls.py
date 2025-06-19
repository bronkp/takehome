from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from endpoint import views
router = routers.DefaultRouter()
router.register(r'device', views.DeviceViewSet)
router.register(r'payload', views.PayloadViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
    