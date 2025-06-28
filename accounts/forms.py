from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import login , logout

class UserRegesterForm(forms.Form):
    first_name = forms.CharField(max_length=80 , widget=(forms.TextInput(attrs={ 'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})))
    username = forms.CharField(max_length=80 , widget=(forms.TextInput(attrs={ 'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})))
    email_user = forms.EmailField(max_length=100 , widget=(forms.EmailInput(attrs={ 'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})))
    password1 = forms.CharField(max_length=80 , widget=(forms.PasswordInput(attrs={ 'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})))
    password2  = forms.CharField(max_length=80 , widget=(forms.PasswordInput(attrs={ 'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})))
    
    #check email
    def clean_email_user(self):
        email = self.cleaned_data['email_user']
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use")
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username is already in use")
        return username

    
    #check verify password1 and password2
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("رمز عبورها یکسان نیستند.")



class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=80 , widget=(forms.TextInput(attrs={ 'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})))
    password = forms.CharField(max_length=80 , widget=(forms.PasswordInput(attrs={ 'class': 'block w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500'})))    

