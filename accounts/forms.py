from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class UserRegesterForm(forms.Form):
    first_name = forms.CharField(max_length=80 , widget=(forms.TextInput(attrs={'class':'form-control'})))
    username = forms.CharField(max_length=80 , widget=(forms.TextInput(attrs={'class':'form-control'})))
    email_user = forms.EmailField(max_length=100 , widget=(forms.EmailInput(attrs={'class':'form-control'})))
    password1 = forms.CharField(max_length=80 , widget=(forms.PasswordInput(attrs={'class':'form-control'})))
    password2  = forms.CharField(max_length=80 , widget=(forms.PasswordInput(attrs={'class':'form-control'})))
    
    #check email
    def clean_email_user(self):
        email = self.cleaned_data['email_user']
        if User.objects.filter(email=email).exists():
            raise ValidationError("این ایمیل قبلاً ثبت شده است.")
        return email
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("این نام کاربری قبلا استفاده شده است.")
        return username

    
    #check verify password1 and password2
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("رمز عبورها یکسان نیستند.")
