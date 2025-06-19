from django.db import models

# Create your models here.
class Device(models.Model):
    devEUI = models.CharField(unique=True)
    status = models.BooleanField()
    def __str__(self):
        return self.devEUI
class Payload(models.Model):
    device = models.ForeignKey(Device,on_delete=models.CASCADE,related_name="payloads")
    fCnt = models.IntegerField()
    status = models.BooleanField()

    pass