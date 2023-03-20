from django.contrib import admin

from .models import Doctor,Patient,Appointment,Time_Slot

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Time_Slot)
