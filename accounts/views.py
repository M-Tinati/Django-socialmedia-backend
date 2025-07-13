from django.contrib import messages
from django.shortcuts import render, redirect , get_object_or_404
from django.views import View
from .forms import *
from .models import *
from django.contrib.auth.models import User 
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth import views as auth_view
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
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
    
    
    
# class UserProfileView(LoginRequiredMixin,View):
#     template_name = 'accounts/userprofile.html'
#     def get(self,request,user_id):
#         user = User.objects.get(id=user_id)
#         return render (request,self.template_name,{user:'user'})
    
    

    
class UserProfileView(LoginRequiredMixin, View):
    template_name = 'accounts/userprofile.html'
    
    def get(self, request, user_id):
        is_following = False
        user = User.objects.get(id=user_id)
        relation = Follow.objects.filter(from_user=request.user,to_user=user)
        if relation.exists():
            is_following = True
        posts = Post.objects.filter(user=user).order_by('-created')
        return render(request, self.template_name, {'profile_user': user, 'posts': posts , 'is_following':is_following})

class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        if post.user_id == request.user.id:
            post.delete()
        return redirect('accounts:user_profile', user_id=request.user.id)

    

class PostUpdateView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        if post.user != request.user:
            return redirect('home:main')
        form = PostUpdateForm(instance=post)
        return render(request, 'accounts/post_update.html', {'form': form, 'post': post})

    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        if post.user != request.user:
            return redirect('home:main')
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('accounts:user_profile', user_id=request.user.id)
        return render(request, 'accounts/post_update.html', {'form': form, 'post': post})



class PostCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = PostCreateForm()
        return render(request, 'accounts/post_create.html', {'form': form})

    def post(self, request):
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('accounts:user_profile', user_id=request.user.id)
        return render(request, 'accounts/post_create.html', {'form': form})


class UserPasswordReset(auth_view.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('accounts:password_reset_done')


class UserPasswordResetDone(auth_view.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class UserPasswordResetConfirm(auth_view.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete') 


class UserPasswordResetComplete(auth_view.PasswordResetCompleteView): 
    template_name = 'accounts/password_reset_complete.html' 

    


class FollowUserView(LoginRequiredMixin,View):
    def get(self,request,user_id):
        users = User.objects.get(id=user_id)
        relation = Follow.objects.filter(from_user=request,to_user=users)
        if relation.exists():
            messages.error(request,'you already followed this user ','error')
        else:
            relation(from_user=request,to_user=users).save()
            messages.success(request,'you follow this user','success')
        return redirect('accounts:user_profile',user_id)
    
class UnFollowUserView(LoginRequiredMixin,View):
    def get(self,request,user_id):
        users = User.objects.get(id=user_id)
        relation = Follow.objects.filter(from_user=request,to_user=users)
        if relation.exists():
            relation.delete()
            messages.success(request,'you unfollow this user','success')
        else:
            messages.error(request,'error proccess ','error')
        return redirect('accounts:user_profile',user_id)
            
            
    
            