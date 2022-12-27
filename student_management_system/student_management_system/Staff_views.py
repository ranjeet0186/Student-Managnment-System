# import render Module file for help HTML Templates File
from django.shortcuts import redirect, render
from members.models import Staff_Notification, Staff_leave, Staff_feedback, Session_Year,Subject,Student, Staff, Attendance,Attendance_Report, StudentResult, Staffdesign, StaffCopywrite,Staffpatient,Amcat,Nptel  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage





@login_required(login_url='/')
def HOME(request):
    return render(request, 'Staff/home.html')

@login_required(login_url='/')
def NOTIFICATIONS(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id_id = i.id
        notification =  Staff_Notification.objects.filter(staff_id = staff_id_id)
        
        context = {
            'notification':notification,
        }
        return render(request, 'Staff/notification.html', context)

@login_required(login_url='/')  
def STAFF_NOTIFICATION_MARK_AS_DONE(request, status):
    notification = Staff_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('notifications')

@login_required(login_url='/')
def STAFF_APPLY_LEAVE(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id
        
        staff_leave_history = Staff_leave.objects.filter(staff_id = staff_id)
        context = {
            'staff_leave_history':staff_leave_history
        }
    return render(request, 'Staff/apply_leave.html',context)

@login_required(login_url='/')
def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method =="POST":
        
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        
        staff = Staff.objects.get(admin = request.user.id)
        leave = Staff_leave(
            staff_id = staff,
            date = leave_date,
            message = leave_message
        )
        leave.save()
        messages.success(request, 'Staff Leave Apply Successfully Sent !')
        return redirect('staff_apply_leave')
  
@login_required(login_url='/')  
def STAFF_FEEDBACK(request):
    staff_id = Staff.objects.get(admin = request.user.id)
    feedback_history = Staff_feedback.objects.filter(staff_id = staff_id)
    
    context = {
        'feedback_history':feedback_history
    }
    return render(request, 'Staff/feedback.html',context)
    
@login_required(login_url='/')
def STAFF_FEEDBACK_SAVE(request):
     if request.method =="POST":
        feedback = request.POST.get('feedback')
        staff = Staff.objects.get(admin = request.user.id)
        
        feedback = Staff_feedback(
            staff_id = staff,
            feedback = feedback,
            feedback_reply = "",
        )
        feedback.save()
        return redirect( 'staff_feedback')

@login_required(login_url='/') 
def STAFF_TAKE_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin = request.user.id)
    subject = Subject.objects.filter(staff = staff_id)
    sesssion_year = Session_Year.objects.all()
    
    action = request.GET.get('action')
    
    get_subject = None
    get_session_year = None
    students = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            
            get_subject = Subject.objects.get(id = subject_id)
            get_session_year = Session_Year.objects.get(id = session_year_id)
            
            subject = Subject.objects.filter(id = subject_id)
            for i in subject:
                student_id = i.course.id
                students = Student.objects.filter(course_id = student_id)
            
    context = {
        'subject':subject,
        'sesssion_year':sesssion_year,
        'get_subject':get_subject,
        'get_session_year':get_session_year,
        'action':action,
        'students':students,
        
    }
    return render(request, 'Staff/take_attendance.html',context)

@login_required(login_url='/')
def STAFF_SAVE_ATTENDANCE(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        print(subject_id, session_year_id)
        
        attendance_date = request.POST.getlist('attendance_date')
        student_id = request.POST.getlist('student_id') 
        
        get_subject = Subject.objects.get(id = subject_id)
        get_session_year = Session_Year.objects.get(id = session_year_id)
        
        attendance = Attendance(
            subject_id = get_subject,
            attendance_data = attendance_date,
            session_year_id = get_session_year,
        )
        
        attendance.save()
        for i in student_id:
            stud_id = i
            print(stud_id)
            int_stud = int(stud_id)
            
            p_students = Student.objects.get(id = int_stud)
            
            attendance_report = Attendance_Report(
                student_id = p_students,
                attenance_id = attendance,
            )
            attendance_report.save()
            
        
    return redirect('staff_take_attendance')

@login_required(login_url='/')
def STAFF_ADD_RESULT(request):
    staff = Staff.objects.get(admin = request.user)
    subjects = Subject.objects.filter(staff_id = staff)
    session_year = Session_Year.objects.all()
    print(subjects)
    action = request.GET.get('action')
    get_subject = None
    get_session = None
    students = None
    if action is not None:
        if request.method == "POST":
           subject_id = request.POST.get('subject_id')
           session_year_id = request.POST.get('session_year_id')
           

           get_subject = Subject.objects.get(id = subject_id)
           get_session = Session_Year.objects.get(id = session_year_id)

           subjects = Subject.objects.filter(id = subject_id)
           for i in subjects:
               student_id = i.course.id
               students = Student.objects.filter(course_id = student_id)


    context = {
        'subjects':subjects,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session':get_session,
        'students':students,
    }
    return render(request, 'Staff/add_result.html',context)


@login_required(login_url='/')
def STAFF_SAVE_RESULT(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        student_id = request.POST.get('student_id')
        assigment_mark = request.POST.get('assigment_mark')
        Exam_mark = request.POST.get('Exam_mark')

        get_student = Student.objects.get(admin = student_id)
        get_subject = Subject.objects.get(id=subject_id)

        check_exist = StudentResult.objects.filter(subject_id=get_subject, student_id=get_student).exists()
        if check_exist:
            result = StudentResult.objects.get(subject_id=get_subject, student_id=get_student)
            result.subject_assignment_marks = assigment_mark
            result.subject_exam_marks = Exam_mark
            result.save()
            messages.success(request, "Successfully Updated Result")
            return redirect('staff_add_result')
        else:
            result = StudentResult(
                student_id = get_student,
                subject_id = get_subject,
                exam_mark = Exam_mark,
                assigment_mark = assigment_mark
            )
            result.save()
            messages.success(request, "Successfully Added Result")
            return redirect('staff_add_result')

@login_required(login_url='/')       
def DESIGN(request):
    staff = Staff.objects.filter(admin = request.user.id)
    print(staff)
    context = {
        'staff': staff,
    }
    return render(request, 'Staff/design.html',context)

def DESIGN_ADD(request):
    if request.method == 'POST':
        journal_name = request.POST.get('journal_name')
        product_name = request.POST.get('product_name')
        image_patient = request.FILES.get('image_patient')
        document = request.FILES['document']
        
        staff = Staff.objects.get(admin = request.user.id)
        
        design = Staffdesign(
            staff_id = staff,
            journal_name = journal_name,
            product_name = product_name,
            image_patient = image_patient,
            document = document
            
        )  
        design.save()
        messages.success(request, "Design are Successfully Save")
        
        return redirect('design')
    return render(request, 'Staff/design.html')

def COPYWRITE(request):
    staff = Staff.objects.filter(admin = request.user.id)
    
    staffdesign = Staffdesign.objects.all().order_by('journal_name')[:1]
    print(staff)
    context = {
        'staff': staff,
        'staffdesign': staffdesign,
    }
    if request.method == 'POST':
        copywrite_number = request.POST.get('copywrite_number')
        staff = Staff.objects.get(admin = request.user.id)
        copywrite = StaffCopywrite(
            staff_id = staff,
            copywrite_number = copywrite_number,
            
        )  
        copywrite.save()
        messages.success(request, "CopyWrite are Successfully Save")
        
        return redirect('copywrite')
    
    return render(request, 'Staff/copywrite.html',context)
    

def PATIENT(request):
    staff = Staff.objects.filter(admin = request.user.id)
    staffdesign = Staffdesign.objects.all().order_by('journal_name')[:1]
    context = {
        'staff': staff,
        'staffdesign': staffdesign,
    }
    if request.method == 'POST':
        Abstract_technolgy = request.POST.get('Abstract_technolgy')
        staff = Staff.objects.get(admin = request.user.id)
        
        Abstract_technolgy = Staffpatient(
            staff_id = staff,
            Abstract_technolgy = Abstract_technolgy,
            
        )
        Abstract_technolgy.save()
        messages.success(request, "Abstract Technolgy are Successfully Save")
        
        return redirect('patient')
    return render(request, 'Staff/patient.html',context)
    

def VIEW_PATIENT_DETAIL(request):
    staff = Staff.objects.filter(admin = request.user.id)
    staffdesign = Staffdesign.objects.all()
    staffCopywrite = StaffCopywrite.objects.all().order_by('copywrite_number')[:1]
    staffpatient = Staffpatient.objects.all().order_by('Abstract_technolgy')[:1]
    
    context = {
        'staff': staff,
        'staffdesign': staffdesign,
        'staffCopywrite': staffCopywrite,
        'staffpatient':staffpatient,
    }
    
    return render(request, 'Staff/view_patient_detail.html',context)
    
def AMACAT_SCORE (request):
    if request.method == "POST":
        score_domine = request.POST.get('score_domine')
        score_english = request.POST.get('score_english')
        score_logical = request.POST.get('score_logical')
        score_quatitative = request.POST.get('score_quatitative')
        
        staff = Staff.objects.get(admin = request.user.id)
        
        staff_amacat = Amcat(
            staff_id = staff,
            score_domine = score_domine,
            score_english = score_english,
            score_logical = score_logical,
            score_quatitative = score_quatitative,
        )
        staff_amacat.save()
        messages.success(request, "Amcat are Successfully Save")
        return redirect('amacat_score')
    return render(request, 'Staff/Amacat_Score.html')

def NPTEL (request):  
    if request.method == "POST":
        nptel_course = request.POST.get('nptel_course')
        nptel_session_start = request.POST.get('nptel_session_start')
        nptel_session_end = request.POST.get('nptel_session_end')
        percentage = request.POST.get('percentage')
        certificate_type = request.POST.get('certificate_type')
        upload_certificate = request.FILES['upload_certificate']
        
        staff = Staff.objects.get(admin = request.user.id)
        
        staff_nptel = Nptel(
            staff_id = staff,
            nptel_course = nptel_course,
            nptel_session_start = nptel_session_start,
            nptel_session_end = nptel_session_end,
            percentage = percentage,
            certificate_type = certificate_type,
            upload_certificate = upload_certificate,
        )
        staff_nptel.save()
        messages.success(request, "NPTEL are Successfully Save")
        return redirect('nptel')
    return render(request, 'Staff/NPTEL.html')

