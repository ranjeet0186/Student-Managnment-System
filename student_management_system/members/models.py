from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    
    USER = (
        (1,'HOD'),
        (2,'STAFF'),
        (3,'STUDENT'),    
    )
    user_type = models.CharField(choices=USER, max_length = 50, default = 1)
    profile_pic = models.ImageField(upload_to='media/profile_pic')
    
    
class Course(models.Model):
    name = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name
    
class Session_Year(models.Model):
    session_start = models.CharField(max_length = 100)
    session_end = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.session_start + " To " + self.session_end
    
class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length = 100)
    course_id = models.ForeignKey(Course, on_delete = models.DO_NOTHING)
    session = models.ForeignKey(Session_Year, on_delete = models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    
class Staff(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.admin.username
    
class Subject(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True, null=True)
    update_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name
      
class Staff_Notification(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete = models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    status = models.IntegerField(null = True, default = 0)
    
    def __str__(self):
        return self.staff_id.admin.first_name
    
class Staff_leave(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete = models.CASCADE)
    date = models.CharField(max_length=100)
    message = models.TextField()
    status = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True, null=True)
    update_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.staff_id.admin.first_name + self.staff_id.admin.last_name  
    
class Staff_feedback(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete = models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    status = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True, null=True)
    update_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.staff_id.admin.first_name + " " + self.staff_id.admin.last_name
    
class Student_Notification(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    status = models.IntegerField(null = True, default = 0)
    
    def __str__(self):
        return self.student_id.admin.first_name 
    
class Student_feedback(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    status = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True, null=True)
    update_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.student_id.admin.first_name + " " + self.student_id.admin.last_name
    
class Student_leave(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    date = models.CharField(max_length=100)
    message = models.TextField()
    status = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True, null=True)
    update_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.student_id.admin.first_name + self.student_id.admin.last_name  
    
class Attendance(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete = models.DO_NOTHING)
    attendance_data = models.DateField()
    session_year_id = models.ForeignKey(Session_Year, on_delete = models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add = True, null=True)
    update_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.subject_id.name
    
class Attendance_Report(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.DO_NOTHING)
    attenance_id = models.ForeignKey(Attendance, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.student_id.admin.first_name
        
class StudentResult(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete = models.CASCADE)
    assigment_mark = models.IntegerField()
    exam_mark = models.IntegerField()
    created_at = models.DateField(auto_now_add = True)
    update_at = models.DateField(auto_now_add = True)
    
    def __str__(self):
        return self.student_id.admin.first_name
    
class Staffdesign(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete = models.CASCADE)
    journal_name = models.CharField(max_length = 100)
    product_name = models.CharField(max_length = 100)
    image_patient = models.ImageField(upload_to='media/staff_patient_pic')
    document = models.FileField(null = True)
    
    def __str__(self):
        return self.staff_id.admin.first_name + self.staff_id.admin.last_name
 
class StaffCopywrite(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete = models.CASCADE)
    copywrite_number = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.staff_id.admin.first_name
    
class Staffpatient(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete = models.CASCADE)
    Abstract_technolgy = models.TextField()
    
    def __str__(self):
        return self.staff_id.admin.first_name
    
class Studentdesign(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    journal_name = models.CharField(max_length = 100)
    product_name = models.CharField(max_length = 100)
    image_patient = models.ImageField(upload_to='media/student_design_pic')
    document = models.FileField(null = True)
    
    def __str__(self):
        return self.student_id.admin.first_name

class StudentCopywrite(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    copywrite_number = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.student_id.admin.first_name
    
class Studentpatient(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    Abstract_technolgy = models.TextField()
    
    def __str__(self):
        return self.student_id.admin.first_name
    
class Amcat(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete = models.CASCADE)
    score_domine = models.IntegerField(null = True)
    score_english = models.IntegerField(null = True)
    score_logical = models.IntegerField(null = True)
    score_quatitative = models.IntegerField(null = True)
    
    def __str__(self):
        return self.staff_id.admin.first_name
    
class Nptel(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete = models.CASCADE)
    nptel_course = models.CharField(max_length = 100)
    nptel_session_start = models.CharField(max_length = 100)
    nptel_session_end = models.CharField(max_length = 100)
    percentage = models.IntegerField(null = True)
    certificate_type = models.CharField(max_length=50)
    upload_certificate = models.FileField(null = True)
    
    def __str__(self):
        return self.staff_id.admin.first_name
    
class Student_Amcat(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    score_domine = models.IntegerField(null = True)
    score_english = models.IntegerField(null = True)
    score_logical = models.IntegerField(null = True)
    score_quatitative = models.IntegerField(null = True)
    
    def __str__(self):
        return self.student_id.admin.first_name
    
class Student_Nptel(models.Model):
    student_id = models.ForeignKey(Student, on_delete = models.CASCADE)
    nptel_course = models.CharField(max_length = 100)
    nptel_session_start = models.CharField(max_length = 100)
    nptel_session_end = models.CharField(max_length = 100)
    percentage = models.IntegerField(null = True)
    certificate_type = models.CharField(max_length=50)
    upload_certificate = models.FileField(null = True)
    
    def __str__(self):
        return self.student_id.admin.first_name
    
    
    
    
    
    

    
    
    

    
    