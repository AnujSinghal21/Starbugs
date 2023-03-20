from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.urls import reverse  
from django.contrib.auth import authenticate, login, logout
from .models import requester
from members.models import Account




def index(request):
    bg=Account.objects.get(user=request.user).BloodG
    return render(request,"blood_donate/home.html",{"rows":requester.objects.filter(status=True,blood_group=bg),"flag":0})

def submitblood(request):
    name=request.POST["name"]
    volume=request.POST["volume"]
    try:
        int(volume)
    except ValueError:
        return render(request,"blood_donate/home.html",{"rows":requester.objects.filter(status=True),"flag":1})
        
    bloodgroup=request.POST["bloodgrp"]    
    description=request.POST["text"]

    r = requester(name=name,volume=int(volume),blood_group=bloodgroup,description=description,status=True)
    # return HttpResponseRedirect(reverse("index"))
    r.save()
    
    return HttpResponseRedirect(reverse('blood_donate'))

def donate(request):
    if request.method=='POST':
        receiver=request.POST["receiver"]
        # print(receiver)
        return render(request,"blood_donate/accept.html",{"receiver_id":receiver})

def confirm(request):
    if request.method=='POST':
        if(request.POST["status"]=='Yes'):
            r=requester.objects.get(id=request.POST["id"])
            r.status=False
            r.save()
            return HttpResponseRedirect(reverse(index))
        else:
            return HttpResponseRedirect(reverse(index))


