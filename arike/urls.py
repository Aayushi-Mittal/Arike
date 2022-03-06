from django.contrib import admin
from django.urls import include, path
from arike_manager.views import login, shome, thome


urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/login/", login),
    path("shome/", shome),
    path("thome/", thome),
    # path("home/", login),
    path("__reload__/", include("django_browser_reload.urls")),
]
