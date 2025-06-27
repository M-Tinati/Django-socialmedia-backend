from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import *


class AccountsView(View):
    class_form = UserRegesterForm
    template_name = 'accounts/singin.html'

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
            messages.success(request, ('your profile is create'))
            return redirect('home:main')
        messages.success(request, ('ERROR'))
        return render(request, self.template_name, {'form': form})
