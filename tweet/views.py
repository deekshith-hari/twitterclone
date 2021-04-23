from django.shortcuts import render, redirect
from .models import Tweet
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, DeleteView
from .forms import TweetForm
from accounts.models import Profile



# Create your views here.
'''class TweetListView(LoginRequiredMixin, ListView):
    model = Tweet
    template_name = 'tweet/home.html'
    ordering = ['-created_at']

class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Tweet
    template_name = 'tweet/create.html'
    fields = ['body', ]'''
@login_required
def home(request):
    form = TweetForm()
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        new_tweet = form.save(commit=False)
        new_tweet.name = request.user
        new_tweet.save()
        return redirect('home')

    context = {'tweets' : Tweet.objects.all, 'form':form}
    return render(request, 'tweet/home.html', context)


'''class UpdatePostView(UpdateView):
    model = Tweet
    template_name = 'update.html'
    form_class = EditForm'''

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
        return redirect('home')

    context = {'form':form}
    return render(request, 'tweet/update.html', context)
