"""
URL configuration for drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app1 import urls,views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

#creating router object for ModelViewset
router = DefaultRouter()

#Register CityModelViewSet with Router
router.register('Cityapi',views.CityModelViewSet,basename='City')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('drf/',include('app1.urls')),
    #ModelViewSet Class
   path('',include(router.urls)),

   #to use for login in session authentication
   #we get login butto while accessing browsable api
   path('auth/',include('rest_framework.urls')),

   #token auth url for the user to generate his own token 
   path('gettoken/',obtain_auth_token),

]
