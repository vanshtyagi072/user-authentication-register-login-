from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register_app/', views.register, name='register'),
    path('register_app/login_app/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
