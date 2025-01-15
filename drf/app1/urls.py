from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

#creating router object for Viewset
router = DefaultRouter()

#Register PhoneViewSet with Router
router.register('phoneapi',views.PhoneViewSet,basename='Phone')


####################################

#creating router object for ModelViewset
Monitor_router = DefaultRouter()

#Register PhoneViewSet with Router
router.register('Monitorapi',views.MonitorModelViewSet,basename='Monitor')


####################################




urlpatterns = [
   path('name/',views.Name.as_view()),
   path('iall/',views.Intern_list.as_view()),
   path('sapi/',views.api.as_view()),
   path('iapi/',views.InternApi.as_view()),
   path('iapi/<int:pk>',views.InternApi.as_view()),

   ##############################################


   # separate generic view:-

   path('tapi/',views.TeacherList.as_view()),
   path('tapiCre/',views.TeacherCreate.as_view()),
   path('tapiRetr/<int:pk>/',views.TeacherRetrieve.as_view()),
   path('tapiUpd/<int:pk>/',views.TeacherUpdate.as_view()),
   path('tapiDel/<int:pk>/',views.TeacherDelete.as_view()),

   #Combined GenericAPIView

   path('mapi/',views.ManagerListCreate.as_view()),
   path('mapiRUD/<int:pk>/',views.ManagerRUD.as_view()),



##############################
   #Concrete View Class(single)
   path('lapi/',views.LaptopList.as_view()),
   path('lapic/',views.LaptopCreate.as_view()),
   path('lapir/<int:pk>/',views.LaptopRetrieve.as_view()),
   path('lapiu/<int:pk>/',views.LaptopUpdate.as_view()),
   path('lapid/<int:pk>/',views.LaptopDelete.as_view()),
   path('lapilc/<int:pk>/',views.LaptopLC.as_view()),
   path('lapiRU/<int:pk>/',views.LaptopRU.as_view()),
   path('lapiRD/<int:pk>/',views.LaptopRD.as_view()),
   path('lapiRUD/<int:pk>/',views.LaptopRUD.as_view()),


####################################
   #ViewSetClass
   path('',include(router.urls)),

   #ModelViewSet Class
   path('model/',include(Monitor_router.urls)),

   

]

