# import render Module file for help HTML Templates File
from django.shortcuts import render, redirect
from members.models import Student_Notification, Student, Student_feedback,Student_leave, StudentResult, StudentCopywrite, Studentdesign, Studentpatient, Student_Amcat, Student_Nptel
from django.contrib import messages


def HOME(request):
    return render(request, 'Student/home.html')

def STUDENT_NOTIFICATIONS(request):
    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id = i.id
        notification = Student_Notification.objects.filter(student_id = student_id)
        
        context = {
            'notification':notification
        }
    return render(request, 'Student/notification.html',context)

def STUDENT_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Student_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('student_notifications')

def STUDENT_FEEDBACK(request):
    student_id = Student.objects.get(admin = request.user.id)
    feedback_history = Student_feedback.objects.filter(student_id = student_id)
    context = {
        'feedback_history':feedback_history
    }
    return render(request, 'Student/feedback.html',context)

def STUDENT_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        student_id = Student.objects.get(admin = request.user.id)
        
        feedbacks = Student_feedback(
            student_id = student_id,
            feedback = feedback,
            feedback_reply = ""
            
        )
        feedbacks.save()
        return redirect('student_feedback')
    
def STUDENT_LEAVE(request):
    student = Student.objects.get(admin = request.user.id)
    student_leave_history = Student_leave.objects.filter(student_id = student)
    context = {
        'student_leave_history':student_leave_history
    }    
    
    return render(request, 'Student/apply_leave.html',context)

def STUDENT_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        print(leave_date)
        
        student_id = Student.objects.get(admin = request.user.id)
        student_leave = Student_leave(
            student_id = student_id,
            date = leave_date,
            message = leave_message
        ) 
        student_leave.save() 
        messages.success(request, "Leave Are Successfully Send !")
        return redirect('student_leave')
        
def VIEW_RESULT(request):
    mark = None
    student = Student.objects.get(admin = request.user.id)
    
    result = StudentResult.objects.filter(student_id = student)
    
    for i in result:
        assigment_mark = i.assigment_mark
        exam_mark = i.exam_mark
        mark = assigment_mark + exam_mark
        
    
    context = {
        'result':result,
        'mark':mark,
    }
    return render(request, 'Student/view_result.html',context)


def STUDENT_DESIGN(request):
    student = Student.objects.filter(admin = request.user.id)
    print(student)
    context = {
        'student': student,
    }
    return render(request, 'Student/student_design.html',context)

def STUDENT_DESIGN_ADD(request):
    if request.method == 'POST':
        journal_name = request.POST.get('journal_name')
        product_name = request.POST.get('product_name')
        image_patient = request.FILES.get('image_patient')
        document = request.FILES['document']
        
        student = Student.objects.get(admin = request.user.id)
        
        design = Studentdesign(
            student_id = student,
            journal_name = journal_name,
            product_name = product_name,
            image_patient = image_patient,
            document = document
            
        )  
        design.save()
        messages.success(request, "Design are Successfully Save")
        
        return redirect('student_design')
    return render(request, 'Student/student_design.html')

def STUDENT_COPYWRITE(request):
    student = Student.objects.filter(admin = request.user.id)
    
    studentdesign = Studentdesign.objects.all().order_by('journal_name')[:1]
    print(student)
    context = {
        'student': student,
        'studentdesign': studentdesign,
    }
    if request.method == 'POST':
        copywrite_number = request.POST.get('copywrite_number')
        
        student = Student.objects.get(admin = request.user.id)
        
        copywrite = StudentCopywrite(
            student_id = student,
            copywrite_number = copywrite_number,
            
        )  
        copywrite.save()
        messages.success(request, "CopyWrite are Successfully Save")
        
        return redirect('student_copywrite')
    
    return render(request, 'Student/student_copywrite.html',context)

def STUDENT_PATIENT(request):
    student = Student.objects.filter(admin = request.user.id)
    staffdesign = Studentdesign.objects.all().order_by('journal_name')[:1]
    context = {
        'student': student,
        'studentdesign': staffdesign,
    }
    if request.method == 'POST':
        Abstract_technolgy = request.POST.get('Abstract_technolgy')
        student = Student.objects.get(admin = request.user.id)
        
        Abstract_technolgy = Studentpatient(
            student_id = student,
            Abstract_technolgy = Abstract_technolgy,
            
        )
        Abstract_technolgy.save()
        messages.success(request, "Abstract Technolgy are Successfully Save")
        
        return redirect('student_patient')
    return render(request, 'Student/student_patient.html',context)

def STUDENT_VIEW_PATIENT_DETAIL(request):
    student = Student.objects.filter(admin = request.user.id)
    studentdesign = Studentdesign.objects.all()
    studentCopywrite = StudentCopywrite.objects.all().order_by('copywrite_number')[:1]
    studentpatient = Studentpatient.objects.all().order_by('Abstract_technolgy')[:1]
    
    context = {
        'student': student,
        'studentdesign': studentdesign,
        'studentCopywrite': studentCopywrite,
        'studentpatient':studentpatient,
    }
    return render(request, 'Student/student_view_detail.html',context)


def STUDENT_AMACAT_SCORE (request):
    if request.method == "POST":
        score_domine = request.POST.get('score_domine')
        score_english = request.POST.get('score_english')
        score_logical = request.POST.get('score_logical')
        score_quatitative = request.POST.get('score_quatitative')
        
        student = student.objects.get(admin = request.user.id)
        
        student_amacat = Student_Amcat(
            staff_id = student,
            score_domine = score_domine,
            score_english = score_english,
            score_logical = score_logical,
            score_quatitative = score_quatitative,
        )
        student_amacat.save()
        messages.success(request, "Amcat are Successfully Save")
        return redirect('student_amcat_score')
    return render(request, 'Student/student_amcat_score.html')

def STUDENT_NPTEL(request):
    if request.method == "POST":
        nptel_course = request.POST.get('nptel_course')
        nptel_session_start = request.POST.get('nptel_session_start')
        nptel_session_end = request.POST.get('nptel_session_end')
        percentage = request.POST.get('percentage')
        certificate_type = request.POST.get('certificate_type')
        upload_certificate = request.FILES['upload_certificate']
        
        student = Student.objects.get(admin = request.user.id)
        
        student_nptel = Student_Nptel(
            student_id = student,
            nptel_course = nptel_course,
            nptel_session_start = nptel_session_start,
            nptel_session_end = nptel_session_end,
            percentage = percentage,
            certificate_type = certificate_type,
            upload_certificate = upload_certificate,
        )
        student_nptel.save()
        messages.success(request, "NPTEL are Successfully Save")
        return redirect('student_nptel_score')
    return render(request, 'Student/student_nptel_score.html')