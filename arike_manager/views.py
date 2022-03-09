from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

from arike_manager.forms import CustomUserCreationForm, CustomAuthenticationForm
from arike_manager.models import UserProfile


class UserCreateView(CreateView):
    model = UserProfile
    form_class = CustomUserCreationForm
    template_name = "user/create.html"
    success_url = "/login/"


class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "auth/login.html"
    success_url = "/dashboard/"

class Dashboard(TemplateView):
    template_name = "auth/dashboard.html"