from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='main'),
    path('post/', views.HomePostView.as_view(), name='post'),
    path('like/<int:post_id>/', views.LikeView.as_view(), name='like'),
]
