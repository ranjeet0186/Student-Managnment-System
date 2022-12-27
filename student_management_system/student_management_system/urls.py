"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Import Sitting File
from django.conf import settings

# Import Static Folder in Django
from django.conf.urls.static import static

# Import Hod, Staff, Student .py file in urls
from .import views, Hod_views, Staff_views, Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name = 'base'),
    
    # Login Path
    path('', views.LOGIN, name = 'login'),
    path('doLogin', views.doLogin, name = 'doLogin'),
    path('doLogout', views.doLogout, name = 'logout'),
    
    # Profile update
    path('profile', views.PROFILE, name = 'profile'),
    path('profile/update', views.PROFILE_UPDATE, name = 'profile_update'),
    
    # THIS IS HOD STUDENT
    path('Hod/Home', Hod_views.HOME, name = 'hod_home'),
    path('Hod/Student/Add', Hod_views.ADD_STUDENT, name = 'add_student'),
    path('Hod/Student/View', Hod_views.VIEW_STUDENT, name = 'view_student'),
    path('Hod/Student/Edit/<str:id>', Hod_views.EDIT_STUDENT, name = 'edit_student'),
    path('Hod/Student/Update/', Hod_views.UPDATE_STUDENT, name = 'update_student'),
    path('Hod/Student/delete/<str:admin>', Hod_views.DELETE_STUDENT, name = 'delete_student'),
    
    # THIS IS HOD STAFF SECTION
    path('Hod/Staff/Add', Hod_views.ADD_STAFF, name = 'add_staff'),
    path('Hod/Staff/View', Hod_views.VIEW_STAFF, name = 'view_staff'),
    path('Hod/Staff/Edit/<str:id>', Hod_views.EDIT_STAFF, name = 'edit_staff'),
    path('Hod/Staff/Update', Hod_views.UPDATE_STAFF, name = 'update_staff'),
    path('Hod/Staff/delete/<str:admin>', Hod_views.DELETE_STAFF, name = 'delete_staff'),
    
    # THIS IS HOD COURSE SECTION
    path('Hod/Course/Add', Hod_views.ADD_COURSE, name = 'add_course'),
    path('Hod/Course/View', Hod_views.VIEW_COURSE, name = 'view_course'),
    path('Hod/Course/Edit/<str:id>', Hod_views.EDIT_COURSE, name = 'edit_course'),
    path('Hod/Course/Update', Hod_views.UPDATE_COURSE, name = 'update_course'),
    path('Hod/Course/delete/<str:id>', Hod_views.DELETE_COURSE, name = 'delete_course'),
    
    # THIS IS HOD SUBJECT SECTION
    path('Hod/Subject/Add', Hod_views.ADD_SUBJECT, name = 'add_subject'),
    path('Hod/Subject/View', Hod_views.VIEW_SUBJECT, name = 'view_subject'),
    path('Hod/Subject/Edit/<str:id>', Hod_views.EDIT_SUBJECT, name = 'edit_subject'),
    path('Hod/Subject/Update', Hod_views.UPDATE_SUBJECT, name = 'update_subject'),
    path('Hod/Subject/delete/<str:id>', Hod_views.DELETE_SUBJECT, name = 'delete_subject'),
    
    # THIS IS HOD SESSION SECTION
    path('Hod/Session/Add', Hod_views.ADD_SESSION, name = 'add_session'),
    path('Hod/Session/View', Hod_views.VIEW_SESSION, name = 'view_session'),
    path('Hod/Session/Edit/<str:id>', Hod_views.EDIT_SESSION, name = 'edit_session'),
    path('Hod/Session/Update', Hod_views.UPDATE_SESSION, name = 'update_session'),
    path('Hod/Session/delete/<str:id>', Hod_views.DELETE_SESSION, name = 'delete_session'),
    
    path('Hod/Staff/Send_Notifiction', Hod_views.STAFF_SEND_NOTIFICATION, name = 'staff_send_notification'),
    path('Hod/Staff/Save_Notifiction', Hod_views.SAVE_STAFF_NOTIFICATION, name = 'save_staff_notification'),
    
    path('Hod/Staff/leave_view', Hod_views.STAFF_LEAVE_VIEW, name = 'staff_leave_view'),
    path('Hod/Staff/approve_leave/<str:id>', Hod_views.STAFF_APPROVE_LEAVE, name = 'staff_approve_leave'),
    path('Hod/Staff/disapprove_leave/<str:id>', Hod_views.STAFF_DISAPPROVE_LEAVE, name = 'staff_disapprove_leave'),
    path('Hod/Staff/feedback', Hod_views.STAFF_FEEDBACK, name = 'staff_feedback_reply'),
    path('Hod/Staff/feedback/save', Hod_views.STAFF_FEEDBACK_SAVE, name = 'staff_feedback_reply_save'),
    
    path('Hod/Student/Send_Notification', Hod_views.STUDENT_SEND_NOTIFICATION, name = 'student_send_notification'),
    path('Hod/Student/Save_Notification', Hod_views.SAVE_STUDENT_NOTIFICATION, name = 'save_student_notification'),
    path('Hod/Student/feedback', Hod_views.STUDENT_FEEDBACK, name = 'get_student_feedback'),
    path('Hod/Student/feedback/reply/save', Hod_views.REPLY_STUDENT_FEEDBACK, name = 'reply_student_feedback'),
    
    path('Hod/Student/leave_view', Hod_views.STUDENT_LEAVE_VIEW, name = 'student_leave_view'),
    path('Hod/Student/approve_leave/<str:id>', Hod_views.STUDENT_APPROVE_LEAVE, name = 'student_approve_leave'),
    path('Hod/Student/disapprove_leave/<str:id>', Hod_views.STUDENT_DISAPPROVE_LEAVE, name = 'student_disapprove_leave'),
    
    path('Hod/Student/Student_View_Patient', Hod_views.STUDENT_VIEW_DESIGN, name = 'student_view_design'),
    path('Hod/Staff/Staff_View_Patient', Hod_views.STAFF_VIEW_DESIGN, name = 'staff_view_design'),
    path('Hod/Staff/Staff_View_Patient/Open_patient/<str:id>', Hod_views.STAFF_OPEN_PATIENT, name = 'staff_open_patient'),

    
    
    
    
    
    # THIS IS STAFF SECTION
    path('Staff/Home', Staff_views.HOME, name = 'staff_home'),
    path('Staff/Notifications', Staff_views.NOTIFICATIONS, name = 'notifications'),
    path('Staff/mark_as_done/<str:status>', Staff_views.STAFF_NOTIFICATION_MARK_AS_DONE, name = 'staff_notifiction_mark_as_done'),
    path('Staff/Apply_leave', Staff_views.STAFF_APPLY_LEAVE, name = 'staff_apply_leave'),
    path('Staff/Apply_leave_save', Staff_views.STAFF_APPLY_LEAVE_SAVE, name = 'staff_apply_leave_save'),
    path('Staff/feedback', Staff_views.STAFF_FEEDBACK, name = 'staff_feedback'),
    path('Staff/feedback/Save', Staff_views.STAFF_FEEDBACK_SAVE, name = 'staff_feedback_save'),
    
    path('Staff/Take_Attendance', Staff_views.STAFF_TAKE_ATTENDANCE, name = 'staff_take_attendance'),
    path('Staff/Save_Attendance', Staff_views.STAFF_SAVE_ATTENDANCE, name = 'staff_save_attendance'),
    
    path('Staff/Add_Result', Staff_views.STAFF_ADD_RESULT, name = 'staff_add_result'),
    path('Staff/Save_Result', Staff_views.STAFF_SAVE_RESULT, name = 'staff_save_result'),
    
    # Patient
    path('Staff/Design', Staff_views.DESIGN, name = 'design'),
    path('Staff/Design_Add', Staff_views.DESIGN_ADD, name = 'design_add'),
    path('Staff/CopyWrite', Staff_views.COPYWRITE, name = 'copywrite'),
    path('Staff/Patient', Staff_views.PATIENT, name = 'patient'),
    path('Staff/View_Patient', Staff_views.VIEW_PATIENT_DETAIL, name = 'view_patient_detail'),
    
    path('Staff/Amacat_Score', Staff_views.AMACAT_SCORE, name = 'amacat_score'),
    path('Staff/Nptel', Staff_views.NPTEL, name = 'nptel'),
    
    
    # THIS IS STUDENT SECTION
    path('Student/Home', Student_views.HOME, name = 'student_home'),
    path('Student/Notifications', Student_views.STUDENT_NOTIFICATIONS, name = 'student_notifications'),
    path('Student/mark_as_done/<str:status>', Student_views.STUDENT_NOTIFICATION_MARK_AS_DONE, name = 'student_notifiction_mark_as_done'),
    path('Student/feedback', Student_views.STUDENT_FEEDBACK, name = 'student_feedback'),
    path('Student/feedback/Save', Student_views.STUDENT_FEEDBACK_SAVE, name = 'student_feedback_save'),
    
    path('Student/apply_for_leave', Student_views.STUDENT_LEAVE, name = 'student_leave'),
    path('Student/Leave_save', Student_views.STUDENT_LEAVE_SAVE, name = 'student_leave_save'),
    path('Student/View_Result', Student_views.VIEW_RESULT, name = 'view_result'),
    
    path('Student/Student_Design', Student_views.STUDENT_DESIGN, name = 'student_design'),
    path('Student/Student_Design_Add', Student_views.STUDENT_DESIGN_ADD, name = 'student_design_add'),
    path('Student/Student_CopyWrite', Student_views.STUDENT_COPYWRITE, name = 'student_copywrite'),
    path('Student/Student_Patient', Student_views.STUDENT_PATIENT, name = 'student_patient'),
    path('Student/Student_View_Patient', Student_views.STUDENT_VIEW_PATIENT_DETAIL, name = 'student_view_detail'),
    
    path('Student/Amacat_Score', Student_views.STUDENT_AMACAT_SCORE, name = 'student_amcat_score'),
    path('Student/Nptel', Student_views.STUDENT_NPTEL, name = 'student_nptel_score'),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
