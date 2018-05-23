from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Driver_Profile
from .forms import EditProfile, EditUserForm, CarForm, DepartureForm
import requests
from decouple import config


GOOGLE_MAP_API_KEY = config('GOOGLE_MAP_API_KEY')
IPSTACK_API_KEY = config('IPSTACK_API_KEY')


@login_required(login_url='/accounts/login/')
def home(request, id):
    title = "Driver"
    current_user = request.user
    profile = Driver_Profile.objects.get(name=current_user.id)
    form = DepartureForm()
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
    response = requests.get(f'http://freegeoip.net/json/{ip_address}?access_key={IPSTACK_API_KEY}')
    geodata = response.json()
    context = {
        "title": title,
        "form": form,
        "current_user": current_user,
        "profile": profile,
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': GOOGLE_MAP_API_KEY
        }

    return render(request, 'index.html', context)


@login_required(login_url='/accounts/login/')
@transaction.atomic
def edit_profile(request, id):
    current_user = request.user
    profile = Driver_Profile.objects.get(name=current_user.id)
    if request.method == 'POST':
        profile_form = EditProfile(request.POST, request.FILES, instance=current_user.profile)
        user_form = EditUserForm(request.POST, instance=current_user)
        car_form = CarForm(request.POST, request.FILES, instance=current_user)
        if profile_form.is_valid() and user_form.is_valid() and car_form.is_valid():
            profile = profile_form.save(commit=False)
            user = user_form.save(commit=False)
            car = car_form.save(commit=False)
            profile.user = current_user
            profile.save()
            user.save()
            car.save()
            return redirect('home', current_user.id)
    else:
        profile_form = EditProfile()
        user_form = EditUserForm()
        car_form = CarForm()
    context = {
        "current_user": current_user, "profile_form": profile_form,
        "user_form": user_form, "profile": profile,
        "car_form": car_form}
    return render(request, 'edit-profile.html', context)
