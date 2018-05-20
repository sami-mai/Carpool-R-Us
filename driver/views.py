from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Driver_Profile
from .forms import EditProfile, EditUserForm


@login_required(login_url='/accounts/login/')
def home(request):
    title = "Driver"
    current_user = request.user
    context = {"title": title, "current_user": current_user}

    return render(request, 'index.html', context)


@login_required(login_url='/accounts/login/')
@transaction.atomic
def edit_profile(request, id):
    current_user = request.user
    profile = Driver_Profile.objects.get(name=current_user.id)
    if request.method == 'POST':
        profile_form = EditProfile(request.POST, request.FILES, instance=current_user.profile)
        user_form = EditUserForm(request.POST, instance=current_user)
        if profile_form.is_valid() and user_form.is_valid():
            profile = profile_form.save(commit=False)
            user = user_form.save(commit=False)
            profile.user = current_user
            profile.save()
            user.save()
            return redirect('user_profile', current_user.id)
    else:
        profile_form = EditProfile()
        user_form = EditUserForm()
    context = {"current_user": current_user, "profile_form": profile_form, "user_form": user_form, "profile": profile}
    return render(request, 'edit-profile.html', context)
