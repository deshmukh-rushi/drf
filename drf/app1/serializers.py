from rest_framework import serializers




class EmployeeSerializer(serializers.Serializer):
    emp_id = serializers.IntegerField(primary_key=True)
    emp_name = serializers.CharField(max_length=100)
    emp_city = serializers.CharField(max_length=100)
    emp_phone = serializers.BigIntegerField()