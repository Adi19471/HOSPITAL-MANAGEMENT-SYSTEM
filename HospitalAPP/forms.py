from django import forms
from django.db.models import fields
from .models import Hospital_department,hospital_doctor,hospital_doctor_departments,hospital_patient,hospital_roomKind,hospital_room

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