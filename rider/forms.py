from django import forms
from .models import Rider_Profile, User


class EditProfile(forms.ModelForm):
    class Meta:
        model = Rider_Profile
        fields = ['avatar', 'national_ID']
        exclude = ['name', 'current_location', 'email_confirmed', 'pickup_location']


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
