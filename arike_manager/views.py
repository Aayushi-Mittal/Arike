from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, TemplateView

from arike_manager.forms import MyUserCreationForm, CustomAuthenticationForm
from arike_manager.models import UserProfile

class UserCreateView(CreateView):
    model = UserProfile
    form_class = MyUserCreationForm
    template_name = "user/create.html"
    success_url = "/login"
class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "auth/login.html"


class Dashboard(TemplateView):


class facilityCreationView(CreateView):
    pass

class addPatientView(CreateView):
    pass

class addFamilyDetails(CreateView):
    pass

class addPatientDisease(CreateView):
    pass