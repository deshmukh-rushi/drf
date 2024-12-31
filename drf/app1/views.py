from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.renderers import JSONRenderer
# Create your views here.

class Name(View):
    n = '<h1> My name is Rushi</h1>'
    def get(self,request):
        return HttpResponse(self.n) 
    


class  Employee_details(View):
    emp = Employee.objects.get(emp_id=1)
    serializer = EmployeeSerializer(emp)
    json_data = JSONRenderer().render(serializer.data)
    def get(self,request):
        return HttpResponse(self.json_data,content_type = 'application/json')


#Query set


class  Employee_list(View):
    emp = Employee.objects.all()
    serializer = EmployeeSerializer(emp,many = True)
    json_data = JSONRenderer().render(serializer.data) 
    def get(self,request):
        return HttpResponse(self.json_data,content_type = 'application/json')
