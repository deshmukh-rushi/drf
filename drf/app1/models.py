from django.db import models

# Create your models here.


class Intern(models.Model):
    intern_id = models.IntegerField(primary_key=True)
    intern_name = models.CharField(max_length=50)
    intern_city = models.CharField(max_length=50)
    intern_phone = models.CharField(max_length=10)


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = models.BigIntegerField()  


class Manager(models.Model):
    name =models.CharField(max_length=50)
    city =models.CharField(max_length=50)
    phone =models.BigIntegerField()