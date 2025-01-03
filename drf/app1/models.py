from django.db import models

# Create your models here.

class Employee (models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    emp_city = models.CharField(max_length=100)
    emp_phone = models.BigIntegerField()


    # def __str__(self):
    #     return self.emp_name


class Intern(models.Model):
    intern_id = models.IntegerField(primary_key=True)
    intern_name = models.CharField(max_length=50)
    intern_city = models.CharField(max_length=50)
    intern_phone = models.CharField(max_length=10)


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)