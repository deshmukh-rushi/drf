from django.contrib import admin
from app1.models import Employee,Intern,Student
# Register your models here.



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_id','emp_name', 'emp_city','emp_phone')

@admin.register(Intern)
class InternAdmin(admin.ModelAdmin):
    list_display = ('intern_id','intern_name', 'intern_city','intern_phone')
    
# admin.site.register(Employee, EmployeeAdmin)
# admin.site.register(Intern,InternAdmin)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']