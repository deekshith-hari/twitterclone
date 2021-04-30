from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<int:pk>/', views.update_tweet, name='update_tweet'),
    path('delete/<int:pk>/', views.delete_tweet, name='delete_tweet'),
    path('like_tweet/<int:pk>/', views.like_tweet, name='like_tweet'),
]
