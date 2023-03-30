from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.urls import reverse  
from django.contrib.auth import authenticate, login, logout
from .models import requester
from members.models import Account
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    bg=Account.objects.get(user=request.user).BloodG
    if bg =='A+':
        return render(request,"blood_donate/blood_home.html",{"rows":requester.objects.filter(status=True,blood_group=bg )|requester.objects.filter(status=True,blood_group='AB+' ),"flag":0})
    elif bg =='O+':
        return render(request,"blood_donate/blood_home.html",{"rows":requester.objects.filter(status=True,blood_group=bg )|requester.objects.filter(status=True,blood_group='AB+' )|requester.objects.filter(status=True,blood_group='B+')|requester.objects.filter(status=True,blood_group='A+'),"flag":0})
    elif bg =='B+':
        return render(request,"blood_donate/blood_home.html",{"rows":requester.objects.filter(status=True,blood_group=bg )|requester.objects.filter(status=True,blood_group='AB+' ),"flag":0})
    elif bg =='AB+':
        return render(request,"blood_donate/blood_home.html",{"rows":requester.objects.filter(status=True,blood_group=bg ),"flag":0})
    elif bg =='A-':
        return render(request,"blood_donate/bloogitd_home.html",{"rows":requester.objects.filter(status=True,blood_group=bg )|requester.objects.filter(status=True,blood_group='AB+' )|requester.objects.filter(status=True,blood_group='AB-' )|requester.objects.filter(status=True,blood_group='A+'),"flag":0})
    elif bg =='O-':
        return render(request,"blood_donate/blood_home.html",{"rows":requester.objects.filter(status=True),"flag":0})
    elif bg =='B-':
        return render(request,"blood_donate/blood_home.html",{"rows":requester.objects.filter(status=True,blood_group=bg )|requester.objects.filter(status=True,blood_group='AB+' )|requester.objects.filter(status=True,blood_group='AB-' )|requester.objects.filter(status=True,blood_group='B+'),"flag":0})
    else:
        return render(request,"blood_donate/blood_home.html",{"rows":requester.objects.filter(status=True,blood_group=bg)|requester.objects.filter(status=True,blood_group='AB+' ),"flag":0})

@login_required
def submitblood(request):
    name=request.POST["name"]
    volume=request.POST["volume"]
    try:
        int(volume)
    except ValueError:
        return render(request,"blood_donate/Home.html",{"rows":requester.objects.filter(status=True),"flag":1})
        
    bloodgroup=request.POST["bloodgrp"]    
    description=request.POST["text"]

    r = requester(name=name,volume=int(volume),blood_group=bloodgroup,description=description,status=True)
    # return HttpResponseRedirect(reverse("index"))
    r.save()
    
    return HttpResponseRedirect(reverse('blood_donate'))

@login_required
def donate(request):
    if request.method=='POST':
        receiver=request.POST["receiver"]
        # print(receiver)
        return render(request,"blood_donate/accept.html",{"receiver_id":receiver})

@login_required
def confirm(request):
    if request.method=='POST':
        if(request.POST["status"]=='Yes'):
            r=requester.objects.get(id=request.POST["id"])
            r.status=False
            r.save()
            return HttpResponseRedirect(reverse(index))
        else:
            return HttpResponseRedirect(reverse(index))


