from django.contrib import messages
from django.shortcuts import render, redirect , get_object_or_404
from django.views import *
from accounts.models import *
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
class HomeView(View):
    def get(self,request):
        return render(request, 'home/index.html')
    def post(self,request):
        return render(request, 'home/index.html')
    
    
class HomePostView(View):
    template_name = 'home/homepost.html'
    form_class = SearchForm

    def get(self, request):
        form = self.form_class(request.GET or None)
        posts = Post.objects.select_related('user').order_by('-created')

        if form.is_valid():
            search_term = form.cleaned_data.get('search')
            if search_term:
                posts = posts.filter(body__icontains=search_term)

        return render(request, self.template_name, {
            'posts': posts,
            'form': form
        })

class LikeView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        like = Vote.objects.filter(post=post, user=request.user)

        if like.exists():
            messages.error(request, 'You have already liked this post.')
        else:
            Vote.objects.create(post=post, user=request.user)
            messages.success(request, 'You liked the post successfully!')

        return redirect('home:post')
    