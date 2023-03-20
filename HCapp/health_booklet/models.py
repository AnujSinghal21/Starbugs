from django.db import models
from health.models import Patient, Doctor
# Create your models here.

class HealthRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    disease = models.TextField()
    symptoms = models.TextField()
    prescription = models.TextField()
    comments = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

'''
class HealthRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    disease = models.TextField()
    symptoms = models.TextField()
    prescription = models.TextField()
    comments = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient + self.doctor + self.datetime
'''