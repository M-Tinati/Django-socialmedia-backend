from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.AccountsView.as_view(),name='register_user'),
    path('login/', views.LoginUserView.as_view(),name='login_user'),
    path('logout/', views.LogoutView.as_view(), name='logout_user'),
    path('profile/<int:user_id>' , views.UserProfileView.as_view() , name='user_profile'),
    # path('post/<int:post_id>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:post_id>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

]
