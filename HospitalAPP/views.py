
from django.shortcuts import render,redirect
# import models 
from.models import User, Hospital_department,hospital_doctor,hospital_doctor_departments,hospital_patient,hospital_roomKind,hospital_room
# forms
from.forms import SignupForm,LoginForm,Hospital_departmentForms,hospital_doctordataForms,hospital_doctor_departmentsForm,hospital_patientForm,hospital_roomKindForm,hospital_roomForm


from django.contrib.auth import authenticate,login ,logout as log
from django.contrib import messages

# login registration.logout
def userlogin(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        fm = SignupForm()
    return render(request, 'HOSPITAL/userlogin.html',{'fm':fm})

def login_view(request):
    if request.method =="POST":
        form = LoginForm()
        uname = request.POST.get("username")
        upass = request.POST.get("password")
        
        print("usr name",uname)
        print("password name",upass)
        
        user_data = authenticate(username=uname,password=upass)
        #user_data = authenticate(uname=username,upass=password)
        
        if user_data is not None:
            login(request, user_data)
            return redirect('/')
        else:
            messages.error(request,"your data doesnot match our record")
    
    else:
        form = LoginForm()
    return render(request,'HOSPITAL/loginpage.html',{'user':form})


def logout_view(request):
    
    log(request)
    
    messages.info(request, "Logged out successfully!")
    return redirect('/')
    
    
# ..................................................................complted register login page ,.........................



def home_view(request):
    return render(request, 'HOSPITAL/home.html')

# Hospital_departmentforms {hospital 4}
def HospitalDepartment_view(request):
    if request.method == "POST":
        fm = Hospital_departmentForms(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = Hospital_departmentForms()
    HD = Hospital_department.objects.all()
        

    context ={
        'form': fm,
     'hdepartment': HD
     }
    return render(request, "HOSPITAL/4_HospitalDepartment_view.html", context)

# hopital docytor detailes...............{hospital 5 }
def hospital_doctor_view(request):                                      # levit this concept i will show 
    if request.method == "POST":
        fm = hospital_doctordataForms(request.POST)
        if fm.is_valid():
            fm.save()    
    else:
        fm = hospital_doctordataForms()
    Hd = hospital_doctor.objects.all()
        
        
    return render(request, "HOSPITAL/5_hospital_doctor_view.html", {'form': fm,'form':Hd})

# levit this concept i will show 

# CREATE TABLE hospital_doctor_departments .........-- 6
def hospital_doctor_departments_view(request):
    if request.method == "POST":
        fm = hospital_doctor_departmentsForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_doctor_departmentsForm()
    hdde = hospital_doctor_departments.objects.all()
        

    return render(request, "HOSPITAL/6_hospital_doctor_departments.html",{'form':fm,'hdbe':hdde})


# CREATE TABLE hospital_patient .........................-- 7
def hospital_patient_view(request):
    if request.method == "POST":
        fm = hospital_patientForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_patientForm()
    hpatient = hospital_patient.objects.all()

    return render(request, "HOSPITAL/7_hospital_patient.html",{'form':fm,'hpatient':hpatient})



# CREATE TABLE hospital_roomKind..........-- 8
def hospital_roomKind_view(request):
    if request.method == "POST":
        fm = hospital_roomKindForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_roomKindForm()
    hroom = hospital_roomKind.objects.all()
    return render(request, "HOSPITAL/8_hospital_roomKind.html",{'form':fm,'hroom':hroom}) 

# CREATE TABLE hospital_room......................-- 9
def hospital_room_view(request):
    if request.method == "POST":
        fm = hospital_roomForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
    else:
        fm = hospital_roomForm()
    rooms = hospital_room.objects.all()
    print(rooms)
    return render(request, "HOSPITAL/9_hospital_room.html",{'form':fm,'room':rooms})