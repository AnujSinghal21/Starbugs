from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.urls import reverse  
from django.contrib.auth import authenticate, login, logout
from .models import Bloodrequest,donator
from members.models import Account
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required
def index(request):
    bg=Account.objects.get(user=request.user).BloodG
    if bg =='A+':
        return render(request,"blood_donate/Home.html",{"rows":Bloodrequest.objects.filter(status=True,blood_group=bg )|Bloodrequest.objects.filter(status=True,blood_group='AB+' ),"flag":0})
    elif bg =='O+':
        return render(request,"blood_donate/Home.html",{"rows":Bloodrequest.objects.filter(status=True,blood_group=bg )|Bloodrequest.objects.filter(status=True,blood_group='AB+' )|Bloodrequest.objects.filter(status=True,blood_group='B+')|Bloodrequest.objects.filter(status=True,blood_group='A+'),"flag":0})
    elif bg =='B+':
        return render(request,"blood_donate/Home.html",{"rows":Bloodrequest.objects.filter(status=True,blood_group=bg )|Bloodrequest.objects.filter(status=True,blood_group='AB+' ),"flag":0})
    elif bg =='AB+':
        return render(request,"blood_donate/Home.html",{"rows":Bloodrequest.objects.filter(status=True,blood_group=bg ),"flag":0})
    elif bg =='A-':
        return render(request,"blood_donate/Home.html",{"rows":Bloodrequest.objects.filter(status=True,blood_group=bg )|Bloodrequest.objects.filter(status=True,blood_group='AB+' )|Bloodrequest.objects.filter(status=True,blood_group='AB-' )|Bloodrequest.objects.filter(status=True,blood_group='A+'),"flag":0})
    elif bg =='O-':
        return render(request,"blood_donate/Home.html",{"rows":Bloodrequest.objects.filter(status=True),"flag":0})
    elif bg =='B-':
        return render(request,"blood_donate/Home.html",{"rows":Bloodrequest.objects.filter(status=True,blood_group=bg )|Bloodrequest.objects.filter(status=True,blood_group='AB+' )|Bloodrequest.objects.filter(status=True,blood_group='AB-' )|Bloodrequest.objects.filter(status=True,blood_group='B+'),"flag":0})
    else:
        return render(request,"blood_donate/Home.html",{"rows":Bloodrequest.objects.filter(status=True,blood_group=bg)|Bloodrequest.objects.filter(status=True,blood_group='AB+' ),"flag":0})

@login_required
def submitblood(request):
    name=request.POST["name"]
    volume=request.POST["volume"]
    try:
        int(volume)
    except ValueError:
        return render(request,"blood_donate/Home.html",{"rows":Bloodrequest.objects.filter(status=True),"flag":1})
        
    bloodgroup=request.POST["bloodgrp"]    
    description=request.POST["text"]

    r = Bloodrequest(name=name,volume=int(volume),blood_group=bloodgroup,user=request.user,description=description,status=True)
    # return HttpResponseRedirect(reverse("index"))
    r.save()
    
    return HttpResponseRedirect(reverse('blood_donate'))

@login_required
def closeRequest(request):
    if request.method=='GET':
        receiverReqid=request.GET["Reqid"]
        BloodReq=Bloodrequest.objects.get(id=receiverReqid)
        # print(BloodReq.id)
        return render(request,"blood_donate/accept.html",{"BloodReq":BloodReq})

# many to one
# many are related to 1 like many 
# one to one
# many to many
# one to many
@login_required
def donate(request):
    if request.method=='POST':
        donatorAcc=Account.objects.get(user=request.user)
        donatorobj=donator(name=donatorAcc.user.get_full_name(),email=donatorAcc.user.email,CCID=donatorAcc.CCID)
        donatorobj.save()
        Bloodreq=Bloodrequest.objects.get(id=request.POST["Reqid"])
        Bloodreq.Donator=donatorobj
        Bloodreq.save()
        # print(receiver)
        # ye return karna chiye to same main page
        return HttpResponseRedirect(reverse('blood_donate'))
        # return render(request,"blood_donate/accept.html",{"BloodReqid":receiverReqid})

@login_required
def confirm(request):
    if request.method=='POST':
        if(request.POST["status"]=='Close'):
            r=Bloodrequest.objects.get(id=request.POST["id"])
            print(id)
            print("232")
            r.status=False
            r.save()
            return HttpResponseRedirect(reverse(index))
        else:
            return HttpResponseRedirect(reverse(index))


