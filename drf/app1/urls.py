from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('name/',views.Name.as_view(),name = 'name'),
   path('data/',views.Employee_details.as_view(),name = 'data'),
   path('all/',views.Employee_list.as_view()),
]
