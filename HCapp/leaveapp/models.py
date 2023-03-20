from django.db import models
from django.contrib.auth.models import User
from members.models import Account

status_choices=[
    ('Pending','Pending'),
    ('Approved','Approved'),
    ('Rejected','Rejected'),

]

class Leave_detail(models.Model):
    FromDate=models.DateField()
    ToDate=models.DateField()
    Description=models.TextField(max_length=200)
    #Disease=models.Charfield()
    Prescription_Image=models.ImageField()
    requestTime=models.TimeField(null=True,blank=True)

class LeaveApplication(models.Model):
    Account=models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    Leave_details=models.ForeignKey(Leave_detail,on_delete=models.CASCADE,null=True)
    Status=models.CharField(choices=status_choices,default='Pending',max_length=100,blank=True) 
# Create your models here.
