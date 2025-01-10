from django.db import models

# Create your models here.

#used for normal api using third party application and browsable
class Intern(models.Model):
    intern_id = models.IntegerField(primary_key=True)
    intern_name = models.CharField(max_length=50)
    intern_city = models.CharField(max_length=50)
    intern_phone = models.CharField(max_length=10)

#used for only third party app view
#contain complete process of how the api works
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

#used for Class based View
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = models.BigIntegerField()  

#used for genericViewApi
class Manager(models.Model):
    name =models.CharField(max_length=50)
    city =models.CharField(max_length=50)
    phone =models.BigIntegerField()



    #used for Concrete view class

class Laptop(models.Model):
    brand = models.CharField(max_length=50)
    year = models.IntegerField()
    processor = models.CharField(max_length=20)


#used for ViewSet view class
class Phone(models.Model):
    brand = models.CharField(max_length=50)
    year = models.IntegerField()
    condition = models.CharField(max_length=20)


#used for modelViewSet CLass
class Monitor(models.Model):
    brand = models.CharField(max_length=50)
    year = models.IntegerField()
    condition = models.CharField(max_length=20)