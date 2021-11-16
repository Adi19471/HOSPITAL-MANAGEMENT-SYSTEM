
from django.contrib.auth import authenticate, login, logout as log
from django.contrib import messages
from django.shortcuts import render, redirect
# import models
from .models import Hospital_department, hospital_doctor, hospital_doctor_departments, hospital_patient, hospital_roomKind, hospital_room, hospital_appointment, hospital_roombookings, hospital_patientInsurance, hospital_patientdischargedetails, Hospital_PaymentType, Hospital_patientPayment, hospital_MedcineType, hospital_MedcineBrand, hospital_Medcine, hospital_dischargeMedication, zipCode
# from.models import User, Hospital_department, hospital_doctor, hospital_doctor_departments, hospital_patient, hospital_roomKind, hospital_room, hospital_appointment,
# forms
from.forms import LoginForm,  SignupForm, Hospital_departmentForms, hospital_doctordataForms, hospital_doctor_departmentsForm, hospital_patientForm, hospital_roomKindForm, hospital_roomForm, hospital_appointmentForm, hospital_roombookingsForm, hospital_patientInsuranceForm, hospital_patientdischargedetailsForm, Hospital_PaymentTypeForm, Hospital_patientPaymentForm, hospital_MedcineTypeForm, hospital_MedcineBrandForm, hospital_MedcineForm, hospital_dischargeMedicationForm, zipCodeForm


# login registration.logout


def userlogin(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        fm = SignupForm()
    return render(request, 'HOSPITAL/userlogin.html', {'fm': fm})


def login_view(request):
    if request.method == "POST":
        form = LoginForm()
        uname = request.POST.get("username")
        upass = request.POST.get("password")

        print("usr name", uname)
        print("password name", upass)

        user_data = authenticate(username=uname, password=upass)
        #user_data = authenticate(uname=username,upass=password)

        if user_data is not None:
            login(request, user_data)
            return redirect('/')
        else:
            messages.error(request, "your data doesnot match our record")

    else:
        form = LoginForm()
    return render(request, 'HOSPITAL/loginpage.html', {'user': form})


def logout_view(request):

    log(request)

    messages.info(request, "Logged out successfully!")
    return redirect('/')


# ..................................................................complted register login page ,.........................


def home_view(request):
    return render(request, 'HOSPITAL/home.html')

# Hospital_departmentforms {hospital 4}


def HospitalDepartment_view(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:

            if request.method == "POST":
                fm = Hospital_departmentForms(request.POST)
                if fm.is_valid():
                    fm.save()
            else:
                fm = Hospital_departmentForms()
            HD = Hospital_department.objects.all()

            context = {
                'form': fm,
                'hdepartment': HD
            }
            return render(request, "HOSPITAL/4_HospitalDepartment_view.html", context)

            # if they are not admin
        else:
            return redirect('hospital-doctor')

    # if they are not loggedin
    return redirect("login")


# hopital docytor detailes...............{hospital 5 }


# levit this concept i will show
def hospital_doctor_view(request):
     if request.user.is_authenticated:
        if request.user.is_superuser:

            if request.method == "POST":
                fm = hospital_doctordataForms(request.POST)
                if fm.is_valid():
                    fm.save()
            else:
                fm = hospital_doctordataForms()
            Hd = hospital_doctor.objects.all()

            return render(request, "HOSPITAL/5_hospital_doctor_view.html", {'form': fm, 'form': Hd})
          # if they are not admin
        else:
            return redirect('hospital-doctor')
        
         # if they are not loggedin
     return redirect("login")
# levit this concept i will show


# CREATE TABLE hospital_doctor_departments .........-- 6


def hospital_doctor_departments_view(request):
     if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                fm = hospital_doctor_departmentsForm(request.POST)
                if fm.is_valid():
                    fm.save()
            else:
                fm = hospital_doctor_departmentsForm()
            hdde = hospital_doctor_departments.objects.all()

            return render(request, "HOSPITAL/6_hospital_doctor_departments.html", {'form': fm, 'hdbe': hdde})
     else:
            return redirect('hospital-doctor')
        
         # if they are not loggedin
     return redirect("login")

# CREATE TABLE hospital_patient .........................-- 7
def hospital_patient_view(request):
    if request.method == "POST":
        fm = hospital_patientForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_patientForm()
    hpatient = hospital_patient.objects.all()

    return render(request, "HOSPITAL/7_hospital_patient.html", {'form': fm, 'hpatient': hpatient})


# CREATE TABLE hospital_roomKind..........-- 8
def hospital_roomKind_view(request):
    if request.method == "POST":
        fm = hospital_roomKindForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_roomKindForm()
    hroom = hospital_roomKind.objects.all()
    return render(request, "HOSPITAL/8_hospital_roomKind.html", {'form': fm, 'hroom': hroom})

# CREATE TABLE hospital_room......................-- 9


def hospital_room_view(request):
    if request.method == "POST":
        fm = hospital_roomForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_roomForm()
    rooms = hospital_room.objects.all()

    return render(request, "HOSPITAL/9_hospital_room.html", {'form': fm, 'room': rooms})

# CREATE TABLE hospital_appointment ............-- 10


def hospital_appointment_view(request):
    if request.method == "POST":
        fm = hospital_appointmentForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_appointmentForm()
    appointment = hospital_appointment.objects.all()

    return render(request, "HOSPITAL/10_hospital_appointment.html", {'form': fm, 'appointment': appointment})


# CREATE TABLE hospital_roombookings ............................-- 11
def hospital_roombookings_view(request):
    if request.method == "POST":
        fm = hospital_roombookingsForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_roombookingsForm()
    hroomboking = hospital_roombookings.objects.all()

    return render(request, "HOSPITAL/11_hospital_roombookings.html", {'form': fm, 'hroomboking': hroomboking})

# CREATE TABLE hospital_patientInsurance ................-- 12


def hospital_patientInsurance_view(request):
    if request.method == "POST":
        fm = hospital_patientInsuranceForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_patientInsuranceForm()
    hpatientinsurence = hospital_patientInsurance.objects.all()

    return render(request, "HOSPITAL/12_hospital_patientInsurance.html", {'form': fm, 'hpatientinsurence': hpatientinsurence})

# CREATE TABLE hospital_patientdischargedetails ...........-- 13


def hospital_patientdischargedetails_view(request):
    if request.method == "POST":
        fm = hospital_patientdischargedetailsForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_patientdischargedetailsForm()
    hpatientdischargedeatiles = hospital_patientdischargedetails.objects.all()

    return render(request, "HOSPITAL/13_hospital_patientdischargedetails.html", {'form': fm, 'hpatientdischargedeatiles': hpatientdischargedeatiles})
# CREATE TABLE Hospital_PaymentType...........-- 14


def Hospital_PaymentType_view(request):
    if request.method == "POST":
        fm = Hospital_PaymentTypeForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = Hospital_PaymentTypeForm()
    hpaymenttype = Hospital_PaymentType.objects.all()

    return render(request, "HOSPITAL/14_Hospital_PaymentType.html", {'form': fm, 'hpaymenttype': hpaymenttype})


# CREATE TABLE Hospital_patientPayment............-- 15
def Hospital_patientPayment_view(request):
    if request.method == "POST":
        fm = Hospital_patientPaymentForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = Hospital_patientPaymentForm()
    hpatient = Hospital_patientPayment.objects.all()

    return render(request, "HOSPITAL/15_Hospital_patientPayment.html", {'form': fm, 'hpatient': hpatient})


# CREATE TABLE hospital_MedcineType ......-- 16
def hospital_MedcineType_view(request):
    if request.method == "POST":
        fm = hospital_MedcineTypeForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_MedcineTypeForm()
    hmedicine = hospital_MedcineType.objects.all()

    return render(request, "HOSPITAL/16_hospital_MedcineType.html", {'form': fm, 'hmedicine': hmedicine})


# CREATE TABLE hospital_MedcineBrand ..........-- 17
def hospital_MedcineBrand_view(request):
    if request.method == "POST":
        fm = hospital_MedcineBrandForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_MedcineBrandForm()
    hmedicinebrand = hospital_MedcineBrand.objects.all()

    return render(request, "HOSPITAL/17_hospital_MedcineBrand.html", {'form': fm, 'hmedicinebrand': hmedicinebrand})


# CREATE TABLE hospital_Medcine ..........-- 18
def hospital_Medcine_view(request):
    if request.method == "POST":
        fm = hospital_MedcineForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_MedcineForm()
    hmedicne = hospital_Medcine.objects.all()

    return render(request, "HOSPITAL/18_hospital_Medcine.html", {'form': fm, 'hmedicne': hmedicne})


# CREATE TABLE hospital_dischargeMedication .......-- 19
def hospital_dischargeMedication_view(request):
    if request.method == "POST":
        fm = hospital_dischargeMedicationForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_dischargeMedicationForm()
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
