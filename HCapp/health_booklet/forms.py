from django import forms
from .models import HealthRecord


class HealthRecordForm(forms.ModelForm):
    class Meta:
        model = HealthRecord
        fields = ('disease', 'symptoms','prescription','comments')
