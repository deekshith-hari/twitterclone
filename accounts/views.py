from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Create user
            created_username = form.save()

            # Get the user object created
            created_user = User.objects.get(username=created_username)

            # Craete the profile
            craeted_profile = Profile.objects.create(user=created_user)

            messages.success(request, 'Account Created')

            # Redirect to the update profile page
            update_profile_url = '/profile/update_profile/' + \
                str(craeted_profile.id)
            return redirect(update_profile_url)
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'accounts/profile.html', context)


@login_required
def update_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
            form.save()

            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/update_profile.html', context)
