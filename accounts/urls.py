from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.AccountsView.as_view(),name='register_user'),
    
]
