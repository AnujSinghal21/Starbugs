from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Patient, Doctor, HealthRecord
from .forms import HealthRecordForm
from members.models import Account
from health.models import Appointment
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.

#@login_required
# def option_check(request):
#     # if request.GET["value"] == 'create':
#         # return redirect('add_health_record') 
#     # else: 
#         return render(request,'health_records')
@login_required
def home_health_record(request):
    return render(request,'create_health_record.html',{"submit":0})

@login_required
def add_health_record(request):
    if request.method == 'POST':
        appointment_id=request.POST["id"]
        appointment=Appointment.objects.get(id=appointment_id)
        appointment.status=False
        appointment.save()
    return render(request,'create_health_record.html',{"submit":1})

@login_required
def create_health_record(request):
    if request.method == 'POST':    
        # form = HealthRecordForm(request.POST)
        # if form.is_valid():
        #     health_record = form.save(commit=False)
        #     health_record.patient = patient
        #     health_record.doctor = doctor
        #     health_record.save()
        #     return redirect('health_records', patient_id=patient.id)
        username=request.POST["username1"]
        disease = request.POST["disease"]
        symptoms= request.POST["symptoms"]
        prescription = request.POST["prescription"]
        comment = request.POST["comments"]
        user=request.user
        try:
            user = User.objects.get(username=username)
        except user.DoesNotExist:
            user = None
        if user is None:
            messages.error(request, 'Invalid username')
            return HttpResponseRedirect('/health_booklet/add_health_record?value=create')
        else:
            user = Account.objects.get(user = User.objects.get(username=username))
            patient = Patient.objects.get(user = user)
            doctor = Doctor.objects.get(user=Account.objects.get(user=request.user))
            entry = HealthRecord.objects.create(patient = patient, doctor = doctor, disease = disease,symptoms = symptoms, prescription = prescription, comments = comment)
            entry.save()
       # if not entry.is_valid(): 
    return render(request, 'create_health_record.html',{'submit':1})


@login_required
def view_health_records(request):
    a = request.user
    account = Account.objects.get(user=a).Role
    if(account=="Doctor" or account=="Receptionist"):
        username=request.POST["username"]
        print(username,"!!!!!!!!!!!!!!!!!!!!!!!")
        user = Account.objects.get(user = User.objects.get(username=username))
        print(user)
        patient = Patient.objects.get(user = user)
    elif(account=="Student"):
        patient = Patient.objects.get(user=Account.objects.get(user=request.user))
    else:
        return redirect('home')
    
    health_records = HealthRecord.objects.filter(patient=patient).order_by('-datetime')
    for record in health_records:
        record.date = record.datetime.date()
        record.time = record.datetime.time()

    return render(request, 'view_health_records.html', {'health_records': health_records, 'patient': patient})