from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
# from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from members.models import Account

# Create your models here.


Available_Slots = (
    ("12AM-1AM","12AM-1AM"),
    ("1AM-2AM","1AM-2AM"),
    ("2AM-3AM","2AM-3AM"),
    ("3AM-4AM","3AM-4AM"),
    ("4AM-5AM","4AM-5AM"),
    ("5AM-6AM","5AM-6AM"),
    ("6AM-7AM","6AM-7AM"),
    ("7AM-8AM","7AM-8AM"),
    ("8AM-9AM","8AM-9AM"),
    ("9AM-10AM","9AM-10AM"),
    ("10AM-11AM","10AM-11AM"),
    ("11AM-12AM","11AM-12AM"),
    ("12PM-1PM","12PM-1PM"),
    ("1PM-2PM","1PM-2PM"),
    ("2PM-3PM","2PM-3PM"),
    ("3PM-4PM","3PM-4PM"),
    ("4PM-5PM","4PM-5PM"),
    ("5PM-6PM","5PM-6PM"),
    ("6PM-7PM","6PM-7PM"),
    ("7PM-8PM","7PM-8PM"),
    ("8PM-9PM","8PM-9PM"),
    ("9PM-10PM","9PM-10PM"),
    ("10PM-11PM","10PM-11PM"),
    ("11PM-12PM","11PM-12PM"),
)
Dep1="ENT Specialist"
Dep2="Orthologist"
Dep3="Opthalmologist"
Dep4="Dentist"
Dep5="Cardiologist"
Department_Choices = (
    (Dep1,"ENT Specialist"),
    (Dep2,"Orthologist"),
    (Dep3,"Opthalmologist"),
    (Dep4,"Dentist"),
    (Dep5,"Cardiologist"),
    ("Pathologist","Pathologist"),
)


class Doctor(models.Model):
    user = models.ForeignKey(Account,null=True,on_delete=models.CASCADE)
    # Doctor_Name=models.CharField(max_length=20,null=True)
    #DoctorID=models.IntegerField()
    Department=models.CharField(
        max_length=120,
        choices=Department_Choices,
    )
    Doctor_Name = models.CharField(max_length=50,null=True)
    Post= models.CharField(max_length=60,default="Doctor")

    def __str__(self):
        return self.Doctor_Name
    
    # Available_Time_Slots=models.TimeField()
class Patient(models.Model):
    #emailID,Roll no.
    user = models.ForeignKey(Account,null=True,on_delete=models.CASCADE)
    Patient_Name=models.CharField(max_length=600,null=True)
    # ID=models.IntegerField()

    def __str__(self):
        return self.Patient_Name


class Time_Slot(models.Model):
    starttime = models.IntegerField(null=True)
    total_patient=models.IntegerField(default=0)
    date = models.DateField(null=True)


    doctors=models.ManyToManyField(Doctor)
    
    def __str__(self):
        return str(self.starttime)+":00"+"-"+str(self.starttime+1)+":00"


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,blank = True, null = True , on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,blank = True, null = True , on_delete=models.CASCADE)
    timeSlot = models.ForeignKey(Time_Slot,blank = True, null = True , on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    # hello = models.IntegerField()



# class Appointment(models.Model):
#     Doctor=models.ForeignKey(Doctor, blank=True, null=False, on_delete=models.CASCADE)
#     #we dont need to add department in this class as its already in department
#     Patient=models.ForeignKey(Patient,blank=True,null=True,on_delete=models.CASCADE)
#     # Name=models.CharField('Name',max_length=100,unique=True)
#     Preffered_Appointment_Date= models.DateField(null=True)
# #it is allotted time I think
#     Time_slot= models.TimeField()

#     def __str__(self):
#         return self.Doctor + ' ' + self.Patient+ ' '