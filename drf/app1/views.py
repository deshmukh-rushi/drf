import io
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse,JsonResponse
from app1.serializers import internSerializer,StudentSerializer\
     ,TeacherSerializer,ManagerSerializer,LaptopSerializer,\
     PhoneSerializer,MonitorSerializer,CitySerializer
from .models import Intern,Student,Teacher,Manager\
     ,Laptop,Phone,Monitor,City
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView,\
     ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,\
     ListCreateAPIView,RetrieveDestroyAPIView,\
     RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,\
     RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,\
     TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly\
     ,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly,DjangoObjectPermissions
from .CustomPermission import MyPermission
from app1.customAuth import CutomAuth
# Create your views here.

class Name(View):
    n = '<h1> My name is Rushi</h1>'
    def get(self,request):
        return HttpResponse(self.n) 
    

     
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
    

#Class Based APIView for intern

#@APIView(['GET','POST','PUT','DELETE']):- used for function based view. 

class InternApi(APIView):
        def get(self,request,format = None):
            intern_id = request.data.get('intern_id')
            if intern_id is not None:
                intern = Intern.objects.get(intern_id = intern_id)
                serializer = internSerializer(intern)
                return Response(serializer.data)
            intern = Intern.objects.all()
            serializer = internSerializer(intern,many = True)
            return Response(serializer.data)    
        
        

        def post(self,request,format=None):
            serializer = internSerializer(data = request.data)
            if serializer.is_valid():
                 serializer.save()
                 return Response({'msg':'Data Created'})
            return Response(serializer.errors)
        


        def put(self,request,format=None):
            intern_id = request.data.get('intern_id')
            intern = Intern.objects.get(intern_id = intern_id)
            serializer = internSerializer(intern,data = request.data)
            if serializer.is_valid():
                 serializer.save()
                 return Response({'msg':'complete Data Update '})
            return Response(serializer.errors)
        


        def patch(self,request,format=None):
            intern_id = request.data.get('intern_id')
            intern = Intern.objects.get(intern_id = intern_id)
            serializer = internSerializer(intern,data = request.data)
            if serializer.is_valid():
                 serializer.save()
                 return Response({'msg':'Partial Data Update complete'})
            return Response(serializer.errors)
             


        def delete(self,request,format=None):
            intern_id = request.data.get('intern_id')
            intern = Intern.objects.get(intern_id = intern_id)
            intern.delete()
            return Response({'msg':'data deleted'})
        




        #Generic Api View:-


        #separate:-

class TeacherList(GenericAPIView,ListModelMixin):
             queryset = Teacher.objects.all()
             serializer_class = TeacherSerializer

             def get(self,request,*args,**kwargs):
                  return self.list(request,*args,**kwargs)

class TeacherCreate(GenericAPIView,CreateModelMixin):
     queryset = Teacher.objects.all()
     serializer_class = TeacherSerializer

     def post(self,request,*args,**kwargs):
        return self.create(request,*args, **kwargs)
     

class TeacherRetrieve(GenericAPIView,RetrieveModelMixin):
     queryset = Teacher.objects.all()
     serializer_class = TeacherSerializer

     def get(self, request, *args, **kwargs):
          return self.retrieve(request, *args, **kwargs)
     
class TeacherUpdate(GenericAPIView,UpdateModelMixin):
     queryset = Teacher.objects.all()
     serializer_class = TeacherSerializer

     def put(self, request, *args, **kwargs):
          return self.update(request, *args, **kwargs)
     
class TeacherDelete(GenericAPIView,DestroyModelMixin):
     queryset = Teacher.objects.all()
     serializer_class = TeacherSerializer

     def delete(self,request,*args, **kwargs):
          return self.destroy(request,*args, **kwargs)
     


     #Combined GenricApiView


class ManagerListCreate(GenericAPIView,ListModelMixin,CreateModelMixin):
     queryset = Manager.objects.all()
     serializer_class = ManagerSerializer

     def get(self,request,*args, **kwargs):
          return self.list(request,*args, **kwargs)
     

     def post(self, request, *args, **kwargs):
          return self.create(request, *args, **kwargs)
     
class ManagerRUD(GenericAPIView,DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin):
     queryset = Manager.objects.all()
     serializer_class = ManagerSerializer

     def delete(self,request,*args, **kwargs):
          return self.destroy(request,*args, **kwargs)
     
     def put(self,request,*args, **kwargs):
          return self.update(request,*args,**kwargs)
     
     def get(self,request,*args, **kwargs):
          return self.retrieve(request,*args, **kwargs)
     






#Concrete View Class

class LaptopList(ListAPIView):
     queryset = Laptop.objects.all()
     serializer_class = LaptopSerializer


class LaptopCreate(CreateAPIView):
     queryset = Laptop.objects.all()
     serializer_class = LaptopSerializer

class LaptopRetrieve(RetrieveAPIView):
     queryset = Laptop.objects.all()
     serializer_class = LaptopSerializer

class LaptopUpdate(UpdateAPIView):
     queryset = Laptop.objects.all()
     serializer_class = LaptopSerializer

class LaptopDelete(DestroyAPIView):
     queryset = Laptop.objects.all()
     serializer_class = LaptopSerializer

class LaptopLC(ListCreateAPIView):
     queryset = Laptop.objects.all()
     serializer_class = LaptopSerializer

class LaptopRU(RetrieveUpdateAPIView):
     queryset = Laptop.objects.all()
     serializer_class = LaptopSerializer


class LaptopRD(RetrieveDestroyAPIView):
     queryset = Laptop.objects.all()
     serializer_class = LaptopSerializer
 

class LaptopRUD(RetrieveUpdateDestroyAPIView):
     queryset = Laptop.objects.all()
     serializer_class = LaptopSerializer



     #ViewSet

class PhoneViewSet(viewsets.ViewSet):
     def list(self,request):
          ph = Phone.objects.all()
          seriailzer = PhoneSerializer(ph,many = True)
          return Response(seriailzer.data)
     def retrieve(self,request,pk = None):
          id = pk
          if id is not None:
               ph = Phone.objects.get(id = id)
               serializer = PhoneSerializer(ph)
               return Response(serializer.data)
          
     def create(self,request):
          serializer = PhoneSerializer(data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     
     def update(self,request,pk):
          id = pk
          ph = Phone.objects.get(pk = id)
          serializer = PhoneSerializer(ph,data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response({'msg':'Complete Data Updated'})
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
     
     def partial_update(self,request,pk):
          id = pk
          ph = Phone.objects.get(pk = id)
          serializer = PhoneSerializer(ph,data = request.data,partial = True)
          if serializer.is_valid():
               serializer.save()
               return Response({'msg':'Partial Data Updated'})
          return Response(serializer.errors)
     def destroy(self,request,pk):
          id = pk
          ph = Phone.objects.get(pk = id)
          ph.delete()
          return Response({'msg':'Data Deleted'})
     



#ModelViewSet Class

class MonitorModelViewSet(viewsets.ModelViewSet):
     queryset = Monitor.objects.all()
     serializer_class = MonitorSerializer







#####################################################################
#####################################################################


#Authentication and Permission


#1 Basic Authentication:-

# class CityModelViewSet(viewsets.ModelViewSet):
#      queryset = City.objects.all()
#      serializer_class = CitySerializer
     # authentication_classes =[BasicAuthentication]
     # permission_classes = [IsAuthenticated]

#This is for the if we want to authentic for only a single model
#we can also authenticate for every model
#for that we need to add it in setting.py
#I'll add basic authentication code in setting.py from line 134




#2:- Session Authentication

# class CityModelViewSet(viewsets.ModelViewSet):
#      queryset = City.objects.all()
#      serializer_class = CitySerializer
#      authentication_classes =[SessionAuthentication]
#      permission_classes = [MyPermission]

          #in urls line 36




 #2:- Token Authentication


# class CityModelViewSet(viewsets.ModelViewSet):
#      queryset = City.objects.all()
#      serializer_class = CitySerializer
#      authentication_classes =[TokenAuthentication]
#      permission_classes = [IsAuthenticated]





#####################################################################
#####################################################################
#Custom authentication

#need to create a separte file need to overrideauthentication method


class CityModelViewSet(viewsets.ModelViewSet):
     queryset = City.objects.all()
     serializer_class = CitySerializer
     authentication_classes =[CutomAuth]
     # permission_classes = [IsAuthenticated]

