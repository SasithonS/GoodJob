from django.contrib import admin
from .models import *

@admin.register(JobberUser)
class JobberUserAdmin(admin.ModelAdmin):
    list_display = ['user','name', 'email','phone','address', 'province','hasjob']
    ordering = ['user','name','email','phone','address','province','hasjob']
    search_fields = ['name','email','province__province']

@admin.register(EmployerUser)
class EmployerUserAdmin(admin.ModelAdmin):
    list_display = ['user','name','emp_name' ,'email','phone','address', 'province']
    ordering = ['user','name','emp_name','email','phone','address','province']
    search_fields = ['name','emp_name','email','province__province']

@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = ['user','name','email']
    ordering = ['user','name','email']
    search_fields = ['name','email','email','province__province']

@admin.register(JobberCheck)
class JobberCheckAdmin(admin.ModelAdmin):
    list_display = ['jobber','identity_pic','check_jobber']
    ordering = ['jobber','identity_pic','check_jobber']
    search_fields = ['jobber']

@admin.register(EmployerCheck)
class EmployerCheckAdmin(admin.ModelAdmin):
    list_display = ['employer','identity_pic','check_emp']
    ordering = ['employer','identity_pic','check_emp']
    search_fields = ['employer']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['name','phone','gender','emp_name','province','pay','jobber','apply']
    ordering = ['name','phone','gender','emp_name','province','pay','jobber','apply']
    search_fields = ['name','emp_name']

@admin.register(ApplyJob)
class ApplyJobAdmin(admin.ModelAdmin):
    list_display = ['job','jobber','emp_name','apply_date','check_apply']
    ordering = ['job','jobber','emp_name','apply_date','check_apply']
    search_fields = ['job','jobber','emp_name']

@admin.register(JobberComplain)
class JobberComplainAdmin(admin.ModelAdmin):
    list_display = ['job','jobber','emp_name','subject','complain_date','status']
    ordering = ['job','jobber','emp_name','subject','complain_date','status',]
    search_fields = ['job','jobber','emp_name']

@admin.register(EmployerComplain)
class EmployerComplainAdmin(admin.ModelAdmin):
    list_display = ['job','jobber','emp_name','subject','complain_date','status']
    ordering = ['job','jobber','emp_name','subject','complain_date','status']
    search_fields = ['job','jobber','emp_name']