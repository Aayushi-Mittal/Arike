from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from arike_manager.models import *

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field!="deleted":
                self.fields[field].widget.attrs["class"] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"    
    class Meta:
        model = UserProfile
        fields = ("phone", "is_verified", "role", "facility", "district")


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
        
class FacilityCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field!="deleted":
                self.fields[field].widget.attrs["class"] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"
    class Meta(forms.ModelForm):
        model = Facility
        fields = ("kind", "name", "address", "pincode", "phone", "ward", "deleted")

      
class PatientCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field!="deleted":
                self.fields[field].widget.attrs["class"] = "p-1 mb-2 bg-gray-200/75 rounded-lg w-full"

    class Meta(forms.ModelForm):
        model = Patient
        fields = ("full_name", "date_of_birth", "address", "landmark", "phone", "gender", "emergency_phone_number", "ward", "facility", "deleted", "expired_time")
