from django.db import models
from django.contrib.auth.models import User
from members.models import Account

class donator(models.Model):
    name=models.CharField(max_length=60)
    email = models.EmailField()
    CCID = models.CharField(max_length=12)

class Bloodrequest(models.Model):
    # requester_id=models.
    name = models.CharField(max_length=60)
    volume = models.IntegerField()
    blood_group = models.CharField(max_length=3)
    description = models.CharField(max_length=150)
    user = models.ForeignKey(User, null = True,on_delete=models.CASCADE)
    status = models.BooleanField()
    Donator = models.OneToOneField(donator,null=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.name

