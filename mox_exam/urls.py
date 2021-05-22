from django.urls import path
from django.shortcuts import render
from .views import *

from . import views

app_name = 'mox_exam'
urlpatterns = [
    path("", views.index, name="index-page"),
    path("main", views.main, name="main-page"),
      
]