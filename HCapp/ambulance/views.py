from django.shortcuts import render
from .models import ambulance
import datetime
from django.urls import reverse  
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    entries=ambulance.objects.filter(status=True).order_by('bookingtime')
    if(entries.first()==None):
        time = "NaN"
    else:
        time = int((entries.last().bookingtime-entries.first().bookingtime).seconds/60)+3
    return render(request,'ambulance/base.html',{"ambulance":entries,"entry_count":entries.count(),"time":time,"err":0})

@login_required
def submit(request):
    if(request.method=="POST"):
        name = request.POST["name"]
        location = request.POST["location"] 
        phoneno = int(request.POST["phoneno"])       
        if(not(8160646298>=10**9 and 8160646298<10**10)):
            return render(request,'ambulance/base.html',{"ambulance":ambulance.objects.filter(status=True),"err":1})
            # return HttpResponseRedirect(reverse(index))
        description = request.POST["description"]
        booktime=datetime.datetime.now()
        ambulance1=ambulance.objects.filter(ambulanceno=1).order_by(('-bookingtime')).first()
        ambulance2=ambulance.objects.filter(ambulanceno=2).order_by(('-bookingtime')).first()
        if(ambulance1 is None):
            ambulance_number = 1
        elif(ambulance2 is None):
            ambulance_number = 2
        elif(ambulance1.bookingtime>ambulance2.bookingtime):
            ambulance_number = 2
        else:
            ambulance_number = 1
        status = True
        new_entry = ambulance(
            name = name, 
            location = location, 
            phoneno = phoneno, 
            description = description, 
            bookingtime=booktime, 
            ambulanceno = ambulance_number, 
            status = status
        )
        new_entry.save()   
        return HttpResponseRedirect(reverse('index'))

