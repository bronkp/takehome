from django.db import models

class Device(models.Model):
    devEUI = models.CharField(unique=True)
    status = models.BooleanField()
    def __str__(self):
        return self.devEUI
class Payload(models.Model):
    device = models.ForeignKey(Device,on_delete=models.CASCADE,related_name="payloads")
    fCnt = models.IntegerField()
    status = models.BooleanField()
    #there is more data that could be saved from the payload but not neccesary for spec
    def __str__(self):
        return str(self.fCnt)