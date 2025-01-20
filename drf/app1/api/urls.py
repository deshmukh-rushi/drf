from django.urls import path,include
from app1.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('crud',views.SongViewSet,basename='song')

urlpatterns = [
    path('',include(router.urls))
]
