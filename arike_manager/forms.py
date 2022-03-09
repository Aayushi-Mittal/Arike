from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from arike_manager.models import *

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = ("phone", "is_verified", "role", "facility", "district")


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs[
            "class"
        ] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
        self.fields["password"].widget.attrs[
            "class"
        ] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
