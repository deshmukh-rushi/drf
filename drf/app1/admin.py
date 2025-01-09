from django.contrib import admin
from app1.models import Intern,Student,Teacher,Manager
# Register your models here.



@admin.register(Intern)
class InternAdmin(admin.ModelAdmin):
    list_display = ('intern_id','intern_name', 'intern_city','intern_phone')
 
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','phone']


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','phone']