from io import __all__
from rest_framework import serializers
from .models import Intern,Student,Teacher\
    ,Manager,Laptop,Monitor,Phone,City,Developer,Singer,song



class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        #print(instance.name)
        instance.name = validated_data.get('name',instance.name)
        #print(instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
    

    #Field Level Validation
    def validate_roll(self,value):
        if value >=200:
            raise serializers.ValidationError('Seat Full')
        return value

    #Object Level Validation
    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'samyak' and ct.lower() != 'dharashiv':
            raise serializers.ValidationError('city must be dharashiv')
        return data
    

#using model serializer we can turn below big line of code to the small one


# class internSerializer(serializers.Serializer):
#     intern_id = serializers.IntegerField()
#     intern_name = serializers.CharField(max_length=50)
    # intern_city = serializers.CharField(max_length=50)
    # intern_phone = serializers.CharField(max_length=10) 
# 

    # def create(self,validated_data):
    #         return Student.objects.create(**validated_data)
    
    # def update(self,instance,validated_data):
    #     #print(instance.name)
    #     instance.name = validated_data.get('name',instance.name)
    #     #print(instance.name)
    #     instance.roll = validated_data.get('roll',instance.roll)
    #     instance.city = validated_data.get('city',instance.city)
    #     instance.save()
    #     return instance



    # Model Serializer Class


class internSerializer(serializers.ModelSerializer):
    #validation for name to make it read only
   # intern_name = serializers.CharField(read_only = True)

    #validators
    # def start_with_r(value):
    #     if value['0'].lower() != 'r':
    #         raise serializers.ValidationError('Name Should Start With r')
    # intern_name = serializers.CharField(start_with_r)


    class Meta:
        model = Intern
        fields = ['intern_id','intern_name','intern_city','intern_phone']
    #we can also give validation here for multiple field
       # read_only_fields = ['name','roll']
    #    or
    #     extra_kwargs = {'name':{'read_only':True}}
     
     
     
    #Field Level Validation

    # def validate_roll(self,value):
    #     if value >=200:
    #         raise serializers.ValidationError('Seat Full')
    #     return value

    # #Object Level Validation
    # def validate(self,data):
    #     nm = data.get('name')
    #     ct = data.get('city')
    #     if nm.lower() == 'samyak' and ct.lower() != 'dharashiv':
    #         raise serializers.ValidationError('city must be dharashiv')
    #     return data



class TeacherSerializer(serializers.ModelSerializer):
       class Meta:
            model = Teacher
            fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'


class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = '__all__'

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'



class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = '__all__'



class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'







#serializer relation in drf
# #relatio between model
# class SongSerializer(serializers.ModelSerializer):
#     class  Meta:
#         model = song
#         fields = ['id','title','duration','singer']

# class SingerSerializer(serializers.ModelSerializer):
#     song = serializers.StringRelatedField(many = True,read_only = True)
#     class  Meta:
#         model = Singer
#         fields = ['id','name','gender','song']





#####################################################################
###################################################################


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