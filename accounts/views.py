from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
import logging



# Create your views here.
logger = logging.getLogger(__name__)
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        logger.error(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, 'Account Created')
            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form':form})





@login_required
def profile(request, pk):

    profile = Profile.objects.get(id=pk)
    context = {'profile':profile}
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

    context = {'form':form}
    return render(request, 'accounts/update_profile.html', context)
