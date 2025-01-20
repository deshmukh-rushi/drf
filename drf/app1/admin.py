from django.contrib import admin
from app1.models import Intern,Student,\
    Teacher,Manager,Laptop,Phone,Monitor,City,Developer,Singer,song
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


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ['id','brand','year','processor']

@admin.register(Phone)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ['id','brand','year','condition']

@admin.register(Monitor)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ['id','brand','year','condition']



@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id','name','pincode','country']


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['id','name','designation','city','passby']



@admin.register(Singer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['id','name','gender']



@admin.register(song)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['id','title','singer','duration']