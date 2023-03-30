from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
import json
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Appointment, Doctor, Patient, Time_Slot
from members.models import Account
# from .forms import AppointmentForm
from json import dumps
from django.urls import reverse
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

def assign_roles():
    users = Account.objects.all()
    for user in users:
        if(user.Role == "Student"):
            patient = Patient.objects.filter(user = user)
            if(not patient.exists()):
                name = user.user.first_name + " " + user.user.last_name
                new_patient = Patient(user = user, Patient_Name = name)  
                new_patient.save()

        elif (user.Role == "Doctor"):
            doctor = Doctor.objects.filter(user = user)
            if(not doctor.exists()):
                name = user.user.first_name + " " + user.user.last_name
                new_doctor = Doctor(user = user, Doctor_Name = name)  
                new_doctor.save()
        else:
            patient = Patient.objects.filter(user = user)
            if(not patient.exists()):
                name = user.user.first_name + " " + user.user.last_name
                new_patient = Patient(user = user, Patient_Name = name)  
                new_patient.save()
    return 



def home(request):
    assign_roles()
    # return render(request,'health/home.html',{'appointments':appointments})
    return render(request,'health/Home.html')

@login_required
def getappointments(request):
    user=Account.objects.get(user=request.user)
    if(user.Role=="Doctor"):
        doctor = Doctor.objects.get(user = user)
        appointments = Appointment.objects.filter(doctor = doctor,status = True)
        completed_appointments = Appointment.objects.filter(doctor = doctor,status = False).count()

    else:
        patient = Patient.objects.get(user = user)
        appointments = Appointment.objects.filter(patient = patient,status = True)
        completed_appointments = Appointment.objects.filter(patient = patient,status = False).count()

    return appointments , completed_appointments

@login_required
def book_appointment(request):    
    assign_roles()
    appointments,count_completed = getappointments(request)
    
    # submitted = False
    # if request.method=='POST':
    #     # form=AppointmentForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,"Your Appointment has been booked")
    #         return HttpResponseRedirect('/book_appointment?submitted=True')
    # else:
    #     form=AppointmentForm()
    #     if 'submitted' in request.GET:
    #         submitted=True
    
    return render(request,'health/appointment_form.html',{'submit':0,"appointments":appointments,"count":appointments.count(),"completed":count_completed})

@login_required
def submitdate(request):
    if(request.method=="GET"):
        date=request.GET["date"]
        bookedtime=Time_Slot.objects.filter(date=date).order_by("starttime")       
        timeslots=[            
"00:00-01:00",
"01:00-02:00",
"02:00-03:00",
"03:00-04:00",
"04:00-05:00",
"05:00-06:00",
"06:00-07:00",
"07:00-08:00",
"08:00-09:00",
"09:00-10:00",
"10:00-11:00",
"11:00-12:00",
"12:00-13:00",
"13:00-14:00",
"14:00-15:00",
"15:00-16:00",
"16:00-17:00",
"17:00-18:00",
"18:00-19:00",
"19:00-20:00",
"20:00-21:00",
"21:00-22:00",
"22:00-23:00",
"23:00-00:00",
]       
        
        list=[]
        if(bookedtime.exists()):
            # print(bookedtime)
            dict = {}
            for x in bookedtime:
                # if x.total_patient<=
                # print(x.doctors)
                t=(x.doctors.all().values_list('id',flat=True))
                # print(t)
                for doc in t:
                    if doc not in dict.keys():
                        l=[]
                        l.append(timeslots[x.starttime])
                        dict[doc]=l
                    else:
                        dict[doc].append(timeslots[x.starttime])
            
            doctors_ids = Doctor.objects.all().values_list('id',flat=True)
            
            for entry in doctors_ids:
                dir={}
                dir["name"]=Doctor.objects.get(id=entry).Doctor_Name
                dir["dept"]=Doctor.objects.get(id=entry).Department
                if(entry in dict.keys()):
                    dir["slots"]=[en for en in timeslots if en not in dict[entry]]
                else:
                    dir["slots"]=timeslots
                # list.append(timeslots[dir])
                # print(dir)
                list.append(dir)
                
        else:
            for entry in Doctor.objects.all():
                dir={}
                dir["name"]=entry.Doctor_Name
                dir["dept"]=entry.Department
                dir["slots"]=timeslots
                list.append(dir)
        
        # print(list)
        appointments,count_completed = getappointments(request)

        return render(request,'health/appointment_form.html',{'docData':(json.dumps(list)),'submit':1,'date':date,"appointments":appointments,"count":appointments.count(),"completed":count_completed})


@login_required
def submitfinal(request):
    if (request.method=="GET"):
        doctor = request.GET.get("preferreddoc")
        department = request.GET.get("department")
        doc=Doctor.objects.filter(Doctor_Name=str(doctor),Department=department).first()
        # print(doc) 
        timeslot = str(request.GET.get("timeslot"))
        # print(timeslot)
        date = request.GET.get("date1")
        # print(date,"!!!!")
        # date=datetime.date.today()
        break_ts=timeslot.split(":")
        start = int(break_ts[0])
        find=Time_Slot.objects.filter(starttime=start,date=date)
        # print(find.exists())
        # print(start,":",date)
        if(find.exists()):
            print("HI")
            entry = find.first()
            entry.doctors.add(doc)
            entry.total_patient=entry.total_patient+1
            entry.save()
        else:
            entry=Time_Slot.objects.create(starttime=start,date = date,total_patient=1)
            entry.doctors.add(doc)
            entry.save()
        
        patient = Patient.objects.get(user=Account.objects.get(user=request.user))
        new_appointment=Appointment.objects.create(doctor=doc,patient=patient,timeSlot = entry)
        new_appointment.save()
        return HttpResponseRedirect(reverse('book_appointment'))
    # render(request,'health/home.html')


@login_required
def index(request):
    return render(request,'health/index.html')

@login_required(login_url="home")
def show_appointments(request):
    appointment_list = Appointment.objects.all()
    return render(request,'health/show_appointments.html',{'appointment_list':appointment_list})