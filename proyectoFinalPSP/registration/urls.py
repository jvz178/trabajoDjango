from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('registro', views.SignupView.as_view(), name="registro"),
]