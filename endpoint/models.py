from django.db import models

# Create your models here.
class Device(models.Model):
    devEUI = models.CharField()
    status = models.BooleanField()
    
    pass
# class Payload(models.Model):
#     fCnt = models.IntegerField()
#     pass