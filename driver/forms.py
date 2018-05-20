from django import forms
from .models import Driver_Profile, User


class EditProfile(forms.ModelForm):
    class Meta:
        model = Driver_Profile
        fields = ['avatar']
        exclude = ['name', 'departure_time', 'email_confirmed', 'pickup_locations']


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
