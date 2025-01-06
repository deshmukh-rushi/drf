from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse
from .serializers import EmployeeSerializer,internSerializer,StudentSerializer
from .models import Employee,Intern,Student
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.decorators import method_decorator
import io
from django.views.decorators.csrf import csrf_exempt
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
    
     
class Intern_list(View):
    inte = Intern.objects.all()
    serializer = internSerializer(inte,many = True)
    json_data = JSONRenderer().render(serializer.data)
    def get(self,request):
        return HttpResponse(self.json_data,content_type = 'application/json')
    


# @csrf_exempt - this is used for the function based view

@method_decorator(csrf_exempt, name='dispatch')

class api(View):
    def get(self,request):
       # if request.method == 'GET':
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get('id',None)


            if id is not None:
                stu = Student.objects.get(id = id)
                serializer = StudentSerializer(stu) 
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data,content_type = 'application/json')
            
            
            stu = Student.objects.all()
            serializer = StudentSerializer(stu,many = True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type = 'application/json')
        
    def post(self,request):
       # if request.method == 'POST':
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            serializer = StudentSerializer(data = pythondata)


            if serializer.is_valid():
                serializer.save()
                res = {'msg':'Data Created'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data,content_type = 'application/json')
            

            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type = 'application/json')
            


    def put(self,request):
        if request.method == 'PUT':
            json_data = request.body
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get('id')
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu,data = pythondata,partial = True)
            
            
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Data Updated!!'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data,content_type='application/json')
            
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type = 'application/json') 
        


    def delete(self,request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        res = {'msg': 'data deleted!!'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type = 'application/json')
    #without writing above 2 lines we can write only one which is written below

        return JsonResponse(res, safe = False)