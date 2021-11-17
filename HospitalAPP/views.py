from django.contrib.auth import authenticate, login, logout as log
from django.contrib import messages
from django.shortcuts import render, redirect,HttpResponseRedirect,HttpResponse
# import models
from .models import Hospital_department, hospital_doctor, hospital_doctor_departments, hospital_patient, hospital_roomKind, hospital_room, hospital_appointment, hospital_roombookings, hospital_patientInsurance, hospital_patientdischargedetails, Hospital_PaymentType, Hospital_patientPayment, hospital_MedcineType, hospital_MedcineBrand, hospital_Medcine, hospital_dischargeMedication, zipCode
# from.models import User, Hospital_department, hospital_doctor, hospital_doctor_departments, hospital_patient, hospital_roomKind, hospital_room, hospital_appointment,
# forms
from.forms import SignUpForm,LoginForm, Hospital_departmentForms, hospital_doctorForm, hospital_doctor_departmentsForm, hospital_patientForm, hospital_roomKindForm, hospital_roomForm, hospital_appointmentForm, hospital_roombookingsForm, hospital_patientInsuranceForm, hospital_patientdischargedetailsForm, Hospital_PaymentTypeForm, Hospital_patientPaymentForm, hospital_MedcineTypeForm, hospital_MedcineBrandForm, hospital_MedcineForm, hospital_dischargeMedicationForm, zipCodeForm


# login registration.logout
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# # from django.contrib.auth.models import Group
# from .decorators import auth_users, allowed_users

from django.contrib import messages
# @login_required(login_url='login')

# Logout
def user_logout(request):
 logout(request)
 return HttpResponseRedirect('/login/')

# Sigup
def user_signup(request):
 if request.method == "POST":
  form = SignUpForm(request.POST)
  if form.is_valid():
   user = form.save()
   user.save()
   messages.success(request,"Registration Succesfully Completed")
#    return redirect('/')
 else:
  form = SignUpForm()
 return render(request, 'HOSPITAL/userlogin.html', {'form':form})



# Login
def user_login(request):
 if not request.user.is_authenticated:
  if request.method == "POST":
   form = LoginForm(request=request, data=request.POST)
   if form.is_valid():
    uname = form.cleaned_data['username']
    upass = form.cleaned_data['password']
    user = authenticate(username=uname, password=upass)
    if user is not None:
     login(request, user)
     messages.success(request, 'Logged in Successfully !!')
     return HttpResponseRedirect('/')
  else:
   form = LoginForm()
  return render(request, 'HOSPITAL/loginpage.html', {'form':form})
 else:
  return HttpResponseRedirect('/')


# ..................................................................complted register login page ,.........................


import calendar
import time
import datetime




def home_view(request):
    return render(request, 'HOSPITAL/home.html')

# Hospital_departmentforms {hospital 4}

def HospitalDepartment_view(request):
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)

    myDate = datetime.datetime.now()
    formatedDate = myDate.strftime("%m/%d/%Y")

    initial_data = {
        'id':ts,
      
        }

    
    if request.method == "POST":

        fm = Hospital_departmentForms(request.POST,request.FILES,initial= initial_data,)
        if fm.is_valid():
            fm.save()
    else:
        fm = Hospital_departmentForms(initial=initial_data)
    HD = Hospital_department.objects.all()

    context = {
            'form': fm,
            'hdepartment': HD
        }
    return render(request, "HOSPITAL/4_HospitalDepartment_view.html", context)
   
       
# hopital docytor detailes...............{hospital 5 }

def hospital_doctor_view(request):
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)
    initial_data = {
        'id':ts,
        }
    if request.method == "POST":
        fm = hospital_doctorForm(request.POST,initial=initial_data)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_doctorForm(initial = initial_data)
    all_data = hospital_doctor.objects.all()
    context = {'fm':fm,'all_data':all_data}
    return render(request, "HOSPITAL/5_hospital_doctor_view.html",context)
           
        

# CREATE TABLE hospital_doctor_departments .........-- 6

def hospital_doctor_departments_view(request):
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)
    myDate = datetime.datetime.now()
    formatedDate = myDate.strftime("%m/%d/%Y")
    initial_data = {
        'id':ts, 
        }
    if request.method == "POST":
        fm = hospital_doctor_departmentsForm(request.POST,request.FILES,initial= initial_data,)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_doctor_departmentsForm(initial= initial_data,)
    hdde = hospital_doctor_departments.objects.all()
    return render(request, "HOSPITAL/6_hospital_doctor_departments.html", {'form': fm, 'hdbe': hdde})

   

# CREATE TABLE hospital_patient .........................-- 7

def hospital_patient_view(request):
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)

    myDate = datetime.datetime.now()
    formatedDate = myDate.strftime("%d/%m/%Y")
  

    initial_data = {
        'id':ts,
        'admitDate':formatedDate,
      
        }
   
    if request.method == "POST":
        fm = hospital_patientForm(request.POST, request.FILES,initial= initial_data)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_patientForm(initial= initial_data)
    hpatient = hospital_patient.objects.all()

    return render(request, "HOSPITAL/7_hospital_patient.html", {'form': fm, 'hpatient': hpatient})


# CREATE TABLE hospital_roomKind..........-- 8

def hospital_roomKind_view(request):
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)

    myDate = datetime.datetime.now()
    formatedDate = myDate.strftime("%m/%d/%Y")

    initial_data = {
        'id':ts,
      
        }


    if request.method == "POST":
        fm = hospital_roomKindForm(request.POST, request.FILES,initial= initial_data)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_roomKindForm(initial= initial_data)
    hroom = hospital_roomKind.objects.all()
    return render(request, "HOSPITAL/8_hospital_roomKind.html", {'form': fm, 'hroom': hroom})
 
       
# CREATE TABLE hospital_room......................-- 9
def hospital_room_view(request):
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)

    myDate = datetime.datetime.now()
    formatedDate = myDate.strftime("%m/%d/%Y")

    initial_data = {
        'id':ts,
      
        }

   
    if request.method == "POST":
        fm = hospital_roomForm(request.POST, request.FILES,initial= initial_data)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_roomForm(initial= initial_data)
    rooms = hospital_room.objects.all()

    return render(request, "HOSPITAL/9_hospital_room.html", {'form': fm, 'room': rooms})
 
       
# CREATE TABLE hospital_appointment ............-- 10
def hospital_appointment_view(request):
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)

    myDate = datetime.datetime.now()
    formatedDate = myDate.strftime("%m/%d/%Y")
    initial_data = {
        'id':ts,
        }
    if request.method=="POST":
        fm = hospital_appointmentForm(request.POST, request.FILES,initial= initial_data)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_appointmentForm()
    appointments = hospital_appointment.objects.all()
    return render(request, "HOSPITAL/10_hospital_appointment.html",{'form':fm,'appointments':appointments})

       

# CREATE TABLE hospital_roombookings ............................-- 11
def hospital_roombookings_view(request):
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)

    myDate = datetime.datetime.now()
    formatedDate = myDate.strftime("%m/%d/%Y")

    initial_data = {
        'id':ts,
      
        }
   
    if request.method == "POST":
        fm = hospital_roombookingsForm(request.POST, request.FILES,initial= initial_data)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_roombookingsForm(initial= initial_data)
    hroomboking = hospital_roombookings.objects.all()

    return render(request, "HOSPITAL/11_hospital_roombookings.html", {'form': fm, 'hroomboking': hroomboking})

       
# CREATE TABLE hospital_patientInsurance ................-- 12
def hospital_patientInsurance_view(request):
    
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)

    myDate = datetime.datetime.now()
    formatedDate = myDate.strftime("%m/%d/%Y")

    initial_data = {
        'id':ts,
        'ExpiryDate':formatedDate
      
        }
   
    if request.method == "POST":
    
        fm = hospital_patientInsuranceForm(request.POST, request.FILES,initial= initial_data)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_patientInsuranceForm(initial= initial_data)
    hpatientinsurence = hospital_patientInsurance.objects.all()

    return render(request, "HOSPITAL/12_hospital_patientInsurance.html", {'form': fm, 'hpatientinsurence': hpatientinsurence})

       
# CREATE TABLE hospital_patientdischargedetails ...........-- 13
def hospital_patientdischargedetails_view(request):
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)

    myDate = datetime.datetime.now()
    formatedDate = myDate.strftime("%m/%d/%Y")

    initial_data = {
        'id':ts,
        'admitDate':formatedDate,
        'releaseDate':formatedDate,
      
        }
   
    if request.method == "POST":
        fm = hospital_patientdischargedetailsForm(request.POST, request.FILES,initial= initial_data)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_patientdischargedetailsForm(initial= initial_data)
    hpatientdischargedeatiles = hospital_patientdischargedetails.objects.all()

    return render(request, "HOSPITAL/13_hospital_patientdischargedetails.html", {'form': fm, 'hpatientdischargedeatiles': hpatientdischargedeatiles})

    
# CREATE TABLE Hospital_PaymentType...........-- 14
def Hospital_PaymentType_view(request):
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)

    myDate = datetime.datetime.now()
    formatedDate = myDate.strftime("%m/%d/%Y")

    initial_data = {
        'id':ts,
      
        }
   
    if request.method == "POST":
        fm = Hospital_PaymentTypeForm(request.POST, request.FILES,initial= initial_data)
        if fm.is_valid():
            fm.save()
    else:
        fm = Hospital_PaymentTypeForm(initial= initial_data)
    hpaymenttype = Hospital_PaymentType.objects.all()

    return render(request, "HOSPITAL/14_Hospital_PaymentType.html", {'form': fm, 'hpaymenttype': hpaymenttype})

       

# CREATE TABLE Hospital_patientPayment............-- 15
def Hospital_patientPayment_view(request):
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)

    myDate = datetime.datetime.now()
    formatedDate = myDate.strftime("%m/%d/%Y")

    initial_data = {
        'id':ts,
      
        }
   
    if request.method == "POST":
        fm = Hospital_patientPaymentForm(request.POST, request.FILES,initial= initial_data)
        if fm.is_valid():
            fm.save()
    else:
        fm = Hospital_patientPaymentForm(initial= initial_data)
    hpatient = Hospital_patientPayment.objects.all()

    return render(request, "HOSPITAL/15_Hospital_patientPayment.html", {'form': fm, 'hpatient': hpatient})

    

# CREATE TABLE hospital_MedcineType ......-- 16
def hospital_MedcineType_view(request):
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)

    myDate = datetime.datetime.now()
    formatedDate = myDate.strftime("%m/%d/%Y")

    initial_data = {
        'id':ts,
      
        }
   
    if request.method == "POST":
        fm = hospital_MedcineTypeForm(request.POST, request.FILES,initial= initial_data)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_MedcineTypeForm(initial= initial_data)
    hmedicine = hospital_MedcineType.objects.all()

    return render(request, "HOSPITAL/16_hospital_MedcineType.html", {'form': fm, 'hmedicine': hmedicine})


# CREATE TABLE hospital_MedcineBrand ..........-- 17
def hospital_MedcineBrand_view(request):
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)

    myDate = datetime.datetime.now()
    formatedDate = myDate.strftime("%m/%d/%Y")

    initial_data = {
        'id':ts,
      
        }
   
    if request.method == "POST":
        fm = hospital_MedcineBrandForm(request.POST, request.FILES,initial= initial_data)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_MedcineBrandForm(initial= initial_data)
    hmedicinebrand = hospital_MedcineBrand.objects.all()

    return render(request, "HOSPITAL/17_hospital_MedcineBrand.html", {'form': fm, 'hmedicinebrand': hmedicinebrand})

    

# CREATE TABLE hospital_Medcine ..........-- 18
def hospital_Medcine_view(request):
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)

    myDate = datetime.datetime.now()
    formatedDate = myDate.strftime("%m/%d/%Y")

    initial_data = {
        'id':ts,
      
        }
   
    if request.method == "POST":
        fm = hospital_MedcineForm(request.POST, request.FILES,initial= initial_data)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_MedcineForm(initial= initial_data)
    hmedicne = hospital_Medcine.objects.all()

    return render(request, "HOSPITAL/18_hospital_Medcine.html", {'form': fm, 'hmedicne': hmedicne})

    

# CREATE TABLE hospital_dischargeMedication .......-- 19
def hospital_dischargeMedication_view(request):
    current_GMT = time.gmtime()
    ts = calendar.timegm(current_GMT)

    myDate = datetime.datetime.now()
    formatedDate = myDate.strftime("%m/%d/%Y")

    initial_data = {
        'id':ts,
      
        }
   
    if request.method == "POST":
        fm = hospital_dischargeMedicationForm(request.POST, request.FILES,initial= initial_data)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_dischargeMedicationForm(initial= initial_data)
    hdischargemedicine = hospital_dischargeMedication.objects.all()

    return render(request, "HOSPITAL/19_hospital_dischargeMedication.html", {'form': fm, 'hdischargemedicine': hdischargemedicine})



# CREATE TABLE zipCode ......-- 20
def zipCode_view(request):
   
        if request.method == "POST":
            fm = zipCodeForm(request.POST, request.FILES)
            if fm.is_valid():
                fm.save()
        else:
            fm = zipCodeForm()
        zipcode = zipCode.objects.all()

        return render(request, "HOSPITAL/20_zipCode.html", {'form': fm, 'zipcode': zipcode})
  


