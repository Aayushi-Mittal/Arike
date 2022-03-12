from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LogoutView

from arike_manager.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("user/create/", UserCreateView.as_view()),
    path("login/", UserLoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("facility/", FacilityListView.as_view()),
    path("facility/create/", FacilityCreateView.as_view()),
    path("facility/update/<pk>/", FacilityUpdateView.as_view()),
    path("facility/delete/<pk>/", FacilityDeleteView.as_view()),
    path("facility/detail/<pk>/", FacilityDetailView.as_view()),
    path("patient/", PatientListView.as_view()),
    path("patient/create/", PatientCreateView.as_view()),
    path("patient/update/<pk>/", PatientUpdateView.as_view()),
    path("patient/delete/<pk>/", PatientDeleteView.as_view()),
    path("treatment/", TreatmentListView.as_view()),
    path("treatment/create/", TreatmentCreateView.as_view()),
    path("treatment/update/<pk>/", TreatmentUpdateView.as_view()),
    path("treatment/delete/<pk>/", TreatmentDeleteView.as_view()),
    path("family/", FamilyListView.as_view()),
    path("family/create/", FamilyCreateView.as_view()),
    path("family/update/<pk>/", FamilyUpdateView.as_view()),
    path("family/delete/<pk>/", FamilyDeleteView.as_view()),
    path("dashboard/", Dashboard.as_view()),
]
