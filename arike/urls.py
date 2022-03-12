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
    path("dashboard/", Dashboard.as_view()),
]
