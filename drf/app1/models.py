from django.db import models
from django.db import models
# Create your models here.

class Employee (models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    emp_city = models.CharField(max_length=100)
    emp_phone = models.BigIntegerField()


    # def __str__(self):
    #     return self.emp_name