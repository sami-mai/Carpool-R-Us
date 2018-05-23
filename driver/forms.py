from django import forms
from .models import Driver_Profile, User, Car


class EditProfile(forms.ModelForm):
    class Meta:
        model = Driver_Profile
        fields = ['avatar', 'license_number']
        exclude = ['name', 'departure_time', 'email_confirmed', 'pickup_locations']


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('type', 'brand', 'colour', 'plate_num', 'seat_capacity')


class DepartureForm(forms.ModelForm):
    class Meta:
        model = Driver_Profile
        fields = ['destination']
