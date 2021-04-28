from django.shortcuts import render, redirect
from .models import Tweet
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView
from .forms import TweetForm
from accounts.models import Profile
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required
def home(request, *args, **kwargs):
    form = TweetForm()
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        new_tweet = form.save(commit=False)
        new_tweet.name = request.user
        new_tweet.save()
        return redirect('home')

    context = {'tweets' : Tweet.objects.all().order_by('-created_at'), 'form':form, }
    return render(request, 'tweet/home.html', context)


@login_required
def update_tweet(request, pk):
    tweet = Tweet.objects.get(id=pk)
    form = TweetForm(instance=tweet)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        new_tweet = form.save(commit=False)
        new_tweet.name = request.user
        new_tweet.save()
        form.save()
        return redirect('/')

    context = {'form':form}
    return render(request, 'tweet/update.html', context)


@login_required
def delete_tweet(request, pk):
    tweet = Tweet.objects.get(id=pk)
    if request.method == 'POST':
        tweet.delete()
        return redirect('/')

    context = {'item':tweet}
    return render(request, 'tweet/delete.html', context)



def like_tweet(request, pk):
    tweet = Tweet.objects.get(id=pk)
    tweet.likes.add(request.user)
    return HttpResponseRedirect(reverse('home'))
