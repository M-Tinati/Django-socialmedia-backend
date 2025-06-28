from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from django.contrib.auth.models import User 
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
class AccountsView(View):
    class_form = UserRegesterForm
    template_name = 'accounts/register.html'

    def get(self, request):
        form = self.class_form()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(
                username=cd['username'],
                email=cd['email_user'],
                password=cd['password1'],
                first_name=cd['first_name']
            )
            messages.success(request, 'Your profile is created successfully!')
            return redirect('home:main')
        else:
            messages.error(request, 'Please correct the errors below.')
        return render(request, self.template_name, {'form': form})



class LoginUserView(View):
    class_form = LoginUserForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.class_form()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have logged in successfully!')
                return redirect('home:main')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
        return render(request, self.template_name, {'form': form})
    
    
class LogoutView(LoginRequiredMixin , View):
    def get(self,request):
        logout(request)
        messages.success(request, 'You have logged out successfully!')
        return redirect('home:main')