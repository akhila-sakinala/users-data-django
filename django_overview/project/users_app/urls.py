from django.contrib import admin
from django.urls import path
from users_app import views

urlpatterns = [
    path('users/',views.users),
]