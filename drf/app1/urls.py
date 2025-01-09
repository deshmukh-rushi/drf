from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('name/',views.Name.as_view(),name = 'name'),
   path('iall/',views.Intern_list.as_view()),
   path('sapi/',views.api.as_view()),
   path('iapi/',views.InternApi.as_view()),
   path('iapi/<int:pk>',views.InternApi.as_view()),
   # separate generic view:-

   path('tapi/',views.TeacherList.as_view()),
   path('tapiCre/',views.TeacherCreate.as_view()),
   path('tapiRetr/<int:pk>/',views.TeacherRetrieve.as_view()),
   path('tapiUpd/<int:pk>/',views.TeacherUpdate.as_view()),
   path('tapiDel/<int:pk>/',views.TeacherDelete.as_view()),

   #Combined GenericAPIView

   path('mapi/',views.ManagerListCreate.as_view()),
   path('mapiRUD/<int:pk>/',views.ManagerRUD.as_view()),
]

