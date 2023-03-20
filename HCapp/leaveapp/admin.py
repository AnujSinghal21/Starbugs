from django.contrib import admin
from .models import LeaveApplication,Leave_detail
# Register your models here.
admin.site.register(LeaveApplication)
admin.site.register(Leave_detail)