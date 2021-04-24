from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<int:pk>/', views.update_tweet, name='update_tweet'),
    path('delete/<int:pk>/', views.delete_tweet, name='delete_tweet'),


]
