from user.views import register 
from django.urls import path 
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordResetView
)


urlpatterns = [
    path('register/', register, name='register'),
    
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),

    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),


]
