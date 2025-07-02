from django.shortcuts import render
from django.views import View
from accounts.models import Post  
class HomeView(View):
    def get(self,request):
        return render(request, 'home/index.html')
    def post(self,request):
        return render(request, 'home/index.html')
    
    
class HomePostView(View):
    template_name = 'home/homepost.html'
    def get(self, request):
        posts = Post.objects.select_related('user').order_by('-created')
        return render(request, self.template_name, {'posts': posts})
