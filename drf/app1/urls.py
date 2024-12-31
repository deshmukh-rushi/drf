from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('name/',views.Name.as_view(),name = 'name'),
]
