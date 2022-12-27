from django.contrib import admin

# Import All Model in register File
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class UserModel(UserAdmin):
    List_display = ['username','user_type']   

admin.site.register(CustomUser,UserModel)
admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Staff_Notification)
admin.site.register(Staff_leave)
admin.site.register(Staff_feedback)
admin.site.register(Student_Notification)
admin.site.register(Student_feedback)
admin.site.register(Student_leave)
admin.site.register(Attendance)
admin.site.register(Attendance_Report)
admin.site.register(StudentResult)
admin.site.register(Staffdesign)
admin.site.register(StaffCopywrite)
admin.site.register(Staffpatient)
admin.site.register(Studentdesign)
admin.site.register(StudentCopywrite)
admin.site.register(Studentpatient)
admin.site.register(Amcat)
admin.site.register(Nptel)
admin.site.register(Student_Amcat)
admin.site.register(Student_Nptel)















