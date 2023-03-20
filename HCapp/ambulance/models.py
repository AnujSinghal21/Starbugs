from django.db import models
from django.contrib.auth.models import User


class ambulance(models.Model):
    # requester_id=models.
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=69)
    phoneno = models.IntegerField()
    description = models.CharField(max_length=150)
    bookingtime = models.DateTimeField()
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    ambulanceno = models.IntegerField() 
    status = models.BooleanField()
        
    def __str__(self):
        return self.name    

