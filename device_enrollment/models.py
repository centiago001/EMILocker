from django.db import models

class enrolled_device(models.Model):
    customer_name=models.CharField(max_length=25,null=True)
    device_id=models.IntegerField(max_length=10,null=True)
    device_brand=models.CharField(max_length=25,null=True)
    policy_name=models.CharField(max_length=25,null=True)
    lock_status=models.CharField(max_length=25,null=True,default=False)
    qrcode=models.CharField(max_length=100,null=True)
    