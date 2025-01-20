from django.db import models

#####################################
#for signal token auth
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
######################3




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





#####################################################################
#####################################################################


#Authentication and Permission




class City(models.Model):
    name = models.CharField(max_length=50)
    pincode = models.IntegerField()
    country = models.CharField(max_length=20)


#####################################################################
#####################################################################


#Signal auth Code


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance = None,created = False,**kwargs):
    if created:
        Token.objects.create(user=instance)

#################################################
#################################################

#filtering

class Developer(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    passby=models.CharField(max_length=80)
    

#####################################################
#####################################################


#serializer relation in drf
#relatio between model

class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name

 
class song(models.Model):
    title = models.CharField(max_length=50)
    singer = models.ForeignKey(Singer,on_delete=models.CASCADE,related_name='song')
    duration = models.IntegerField()


    def __str__(self):
        return self.title