from app1.models import song,Singer
from app1.api.serializers import SongSerializer,SingerSerializer
from rest_framework import viewsets


class SongViewSet(viewsets.ModelViewSet):
    queryset = song.objects.all()
    serializer_class = SongSerializer

class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer