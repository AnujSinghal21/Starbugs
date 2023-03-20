from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm,AccountForm
from .models import Account
from json import dumps
# Create your views here.

def loginUser(request):
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['Password']
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,"Error")
            return redirect('loginUser')
    else:
        return render(request, 'Signing/login.html', {})


def logoutUser(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect('home')

def registerUser(request):
    if request.method =='POST':
        username=request.POST["Username"]
        password=request.POST["Password"]
        email=request.POST["Email"]
        first_name=request.POST["First_name"]
        last_name=request.POST["Last_name"]
        DOB=request.POST["DOB"]
        BloodG=request.POST["BloodG"]
        CCID=request.POST["CCID"]
        Gender=request.POST["Gender"]
        user=User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()
        acc=Account(user=user,DOB=DOB, Gender = Gender,BloodG=BloodG,CCID=CCID)
        acc.save()
        messages.success(request,"Registration Successful")
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect('home')
            
    else:
        All_accounts = Account.objects.all()
        Usernames = []
        for accounts in All_accounts:
            username = accounts.user.username
            Usernames.append(username)
        Usernames=dumps(Usernames)
        return render(request,'Signing/register.html',{"Usernames":Usernames})