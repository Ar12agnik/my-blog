
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('profile',views.profile,name='profile'),
    path('profile/<str:username>',views.view_profile,name='view_profile'),
]