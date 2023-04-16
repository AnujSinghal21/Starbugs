from django.db import models
from django.contrib.auth.models import User
roles = [
    ('Student','Student'),
    ('Doctor','Doctor'),
    ('Receptionist','Receptionist'),
    ('Ambulance','Ambulance'),
    ('DUGC','DUGC')
]
BloodG=[
    ('A+','A+'),('A-','A-'),
    ('B+','B+'),('B-','B-'),
    ('O+','O+'),('O-','O-'),
    ('AB+','AB+'),('AB-','AB-'),
]

Gender = [
    ('Male','Male'),
    ('Female','Female'),
]

class Account(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Role=models.CharField(max_length=100,choices=roles,default="Student",blank=True)
    DOB=models.DateField(blank=True,null=True)
    BloodG=models.CharField(choices=BloodG,null=True,max_length=20)
    CCID=models.CharField(null=True,max_length=20)
    Gender=models.CharField(null=True,default='Male',max_length=10)
    ContactNo=models.CharField(null=True,blank=True,max_length=13)
    def __str__(self):
        return self.user.username
