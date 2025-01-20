from app1.models import Singer,song
from rest_framework import serializers

 
#nested Serializer
class SongSerializer(serializers.ModelSerializer):
    class  Meta:
        model = song
        fields = ['id','title','duration']

class SingerSerializer(serializers.ModelSerializer):
    song = SongSerializer(many = True,read_only = True)
    class  Meta:
        model = Singer
        fields = ['id','name','gender','song']