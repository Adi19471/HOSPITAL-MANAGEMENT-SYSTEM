from django import forms
from django.db.models import fields
from .models import Hospital_department,hospital_doctor,hospital_doctor_departments,hospital_patient,hospital_roomKind,hospital_room,hospital_appointment,hospital_roombookings,hospital_patientInsurance,hospital_patientdischargedetails,Hospital_PaymentType,Hospital_patientPayment,hospital_MedcineType,hospital_MedcineBrand,hospital_Medcine,hospital_dischargeMedication,zipCode

# login page registration
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm


class SignupForm(forms.ModelForm):


    class Meta:
        first_name = forms.CharField(label="Name", widget=(forms.TextInput(attrs={'class': 'form-control bg-white'}))),
        last_name = forms.CharField(label="Enter Your Last Name", widget=(forms.TextInput(attrs={'class': 'form-control bg-info'}))),
        email = forms.EmailField(label="Enter Your Last Name", widget=(forms.EmailInput(attrs={'class': 'form-control bg-info'}))),
        model=User

        fields=['first_name', 'last_name', 'email', 'username', 'password']
       
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
        

# ----------------------------------------------------
# Hospital_departmentForms 
class Hospital_departmentForms(forms.ModelForm):
    class Meta:
        model = Hospital_department
        fields = '__all__'



# hospital_doctor forms
class hospital_doctordataForms(forms.ModelForm):
    class Meta:
        model = hospital_doctor
        fields = '__all__'


# hospital_doctor_departments 

class hospital_doctor_departmentsForm(forms.ModelForm):
    class Meta:
        model = hospital_doctor_departments
        fields = '__all__'

# hospital_patient
class hospital_patientForm(forms.ModelForm):
    class Meta:
        model = hospital_patient
        fields = '__all__'


# CREATE TABLE hospital_roomKind..........-- 8
class hospital_roomKindForm(forms.ModelForm):
    class Meta:
        model = hospital_roomKind
        fields = '__all__'


# CREATE TABLE hospital_room......................-- 9
class hospital_roomForm(forms.ModelForm):
    class Meta:
        model = hospital_room
        fields = '__all__'

# CREATE TABLE hospital_appointment ............-- 10
class hospital_appointmentForm(forms.ModelForm):
    class Meta:
        model = hospital_appointment
        fields = '__all__'

# CREATE TABLE hospital_roombookings ............................-- 11
class hospital_roombookingsForm(forms.ModelForm):
    class Meta:
        model = hospital_roombookings
        fields = '__all__'

# CREATE TABLE hospital_patientInsurance ................-- 12
class hospital_patientInsuranceForm(forms.ModelForm):
    class Meta:
        model = hospital_patientInsurance
        fields = '__all__'

# CREATE TABLE hospital_patientdischargedetails ...........-- 13
class hospital_patientdischargedetailsForm(forms.ModelForm):
    class Meta:
        model = hospital_patientdischargedetails
        fields = '__all__'

# CREATE TABLE Hospital_PaymentType...........-- 14
class Hospital_PaymentTypeForm(forms.ModelForm):
    class Meta:
        model = Hospital_PaymentType
        fields = '__all__'

# CREATE TABLE Hospital_patientPayment............-- 15
class Hospital_patientPaymentForm(forms.ModelForm):
    class Meta:
        model = Hospital_patientPayment
        fields = '__all__'

# CREATE TABLE hospital_MedcineType ......-- 16
class hospital_MedcineTypeForm(forms.ModelForm):
    class Meta:
        model = hospital_MedcineType
        fields = '__all__'

# CREATE TABLE hospital_MedcineBrand ..........-- 17  
class hospital_MedcineBrandForm(forms.ModelForm):
    class Meta:
        model = hospital_MedcineBrand
        fields = '__all__'

# CREATE TABLE hospital_Medcine ..........-- 18
class hospital_MedcineForm(forms.ModelForm):
    class Meta:
        model = hospital_Medcine
        fields = '__all__'



# CREATE TABLE hospital_dischargeMedication .......-- 19
class hospital_dischargeMedicationForm(forms.ModelForm):
    class Meta:
        model = hospital_dischargeMedication
        fields = '__all__'

# CREATE TABLE zipCode ......-- 20
class zipCodeForm(forms.ModelForm):
    class Meta:
        model = zipCode
        fields = '__all__'
