from io import __all__
from rest_framework import serializers
from .models import Employee,Intern,Student



class EmployeeSerializer(serializers.Serializer):
    emp_id = serializers.IntegerField()
    emp_name = serializers.CharField(max_length=100)
    emp_city = serializers.CharField(max_length=100)
    emp_phone = serializers.IntegerField()


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
    

#using model serializer we can turn above big line of code to the small one


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
    class Meta:
        model = Intern
        fields = ['intern_id','intern_name','intern_city','intern_phone']

     