from django import forms
from profiles.models import Profiles

class Profile_form(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = '__all__'
