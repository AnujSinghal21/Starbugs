from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Account

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    Role_choices =[('Student','Student'),('Doctor','Doctor')]
    Role=forms.ChoiceField(choices=Role_choices)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
    

class AccountForm(forms.ModelForm):
    class Meta:
        model= Account
        fields = ('Role', )
#email,first_name,last_name,role