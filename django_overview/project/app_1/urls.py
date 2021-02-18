from django.contrib import admin
from django.urls import path
from app_1 import views

urlpatterns = [
    path('hello/',views.hello),
    path('how_are_you/',views.howAreYou)
]