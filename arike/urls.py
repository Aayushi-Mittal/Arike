from django.contrib import admin
from django.urls import include, path

from arike_manager.views import UserCreateView, UserLoginView, Dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("user/signup", UserCreateView.as_view()),
    path("user/login/", UserLoginView.as_view()),
    path("dashboard/", Dashboard.as_view()),
]
