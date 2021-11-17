from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile






class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
  'first_name':forms.TextInput(attrs={'class':'form-control'}),
  'last_name':forms.TextInput(attrs={'class':'form-control'}),
  'email':forms.EmailInput(attrs={'class':'form-control'}),
  

  }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address', 'image']
