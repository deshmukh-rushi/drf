from django.contrib import admin
from app1.models import Employee
# Register your models here.

#@admin.register(Employee)

# admin.site.register(Employee)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id','emp_name', 'emp_city','emp_phone')
    
admin.site.register(Employee, EmployeeAdmin)