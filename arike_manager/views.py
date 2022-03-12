from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from arike_manager.forms import *
from arike_manager.models import *


class UserCreateView(CreateView):
    model = UserProfile
    form_class = CustomUserCreationForm
    template_name = "user/create.html"
    success_url = "/login/"


class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "auth/login.html"
    success_url = "/dashboard/"


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "auth/dashboard.html"


# Facility Views

# class AuthorizedFacilityManager(LoginRequiredMixin):
#     login_url = "/login"
#     success_url = "/dashboard"
#     model = Facility

#     def get_queryset(self):
#         return Facility.objects.filter(deleted=False, userprofile=self.request.user)


class FacilityListView(ListView):
    queryset = Facility.objects.filter(deleted=False)
    template_name = "facility/list.html"
    context_object_name = "facility"
    paginate_by = 10

    def get_queryset(self):
        return Facility.objects.filter(deleted=False)


class FacilityCreateView(CreateView):
    model = Facility
    form_class = FacilityCreationForm
    template_name = "facility/create.html"
    success_url = "/facility/"


class FacilityDeleteView(DeleteView):
    model = Facility
    template_name = "CRUD/delete.html"
    success_url = "/facility/"


class FacilityDetailView(DetailView):
    model = Facility
    template_name = "facility/detail.html"


class FacilityUpdateView(UpdateView):
    model = Facility
    form_class = FacilityCreationForm
    template_name = "facility/update.html"
    success_url = "/dashboard/"

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



# Patient Views

# class AuthorizedPatientManager(LoginRequiredMixin):
#     login_url = "/login"
#     success_url = "/dashboard"
#     model = Patient

#     def get_queryset(self):
#         return Patient.objects.filter(deleted=False, userprofile=self.request.user)


class PatientListView(ListView):
    queryset = Patient.objects.filter(deleted=False)
    template_name = "patient/list.html"
    context_object_name = "patient"
    paginate_by = 10

    def get_queryset(self):
        return Patient.objects.filter(deleted=False)


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientCreationForm
    template_name = "patient/create.html"
    success_url = "/patient"


class PatientDeleteView(DeleteView):
    model = Patient
    template_name = "CRUD/delete.html"
    success_url = "/patient"


class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientCreationForm
    template_name = "patient/update.html"
    success_url = "/patient"

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



# Treatment Views

# class AuthorizedTreatmentManager(LoginRequiredMixin):
#     login_url = "/login"
#     success_url = "/dashboard"
#     model = Treatment

#     def get_queryset(self):
#         return Treatment.objects.filter(deleted=False, userprofile=self.request.user)


class TreatmentListView(ListView):
    queryset = Treatment.objects.filter(deleted=False)
    template_name = "treatment/list.html"
    context_object_name = "treatment"
    paginate_by = 10

    def get_queryset(self):
        return Treatment.objects.filter(deleted=False)


class TreatmentCreateView(CreateView):
    model = Treatment
    form_class = TreatmentCreationForm
    template_name = "treatment/create.html"
    success_url = "/treatment"


class TreatmentDeleteView(DeleteView):
    model = Treatment
    template_name = "CRUD/delete.html"
    success_url = "/treatment"


class TreatmentUpdateView(UpdateView):
    model = Treatment
    form_class = TreatmentCreationForm
    template_name = "treatment/update.html"
    success_url = "/treatment"

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
