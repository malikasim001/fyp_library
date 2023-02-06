"""fyp_repository_systems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.conf import  settings

from fyp_repository_app import views, hodviews, dep_admin_views, student_views, supervisors_views
from fyp_repository_systems import settings
urlpatterns = [
    path('',views.ShowLoginPage,name="ShowLoginPage"),
    path('dologin', views.DoLogin,name="dologin"),
    path('baseclass', hodviews.BaseClass,name="baseclass"),
    path('add_admin',hodviews.AddAdmin,name="add_admin"),
    path('manage_admin',hodviews.Manage_Admin,name="manage_admin"),
    path('admin_save',hodviews.Admin_Save,name="admin_save"),
    path('edit_admin/<str:admin_id>',hodviews.Edit_Admin,name="edit_admin"),
    path('edit_admin_save',hodviews.Edit_admin_Save,name="edit_admin_save"),
    path('addsupervisor',hodviews.AddSupervisor,name="addsupervisor"),
    path('supervisor_save',hodviews.Add_Supervisor_Save,name="supervisor_save"),
    path('manage_supervisor', hodviews.Manage_Supervisor, name="manage_supervisor"),
    path('edit_supervisor/<str:supervisor_id>', hodviews.Edit_Supervisor, name="edit_supervisor"),
    path('edit_supervisor_save', hodviews.Edit_Supervisor_Save, name="edit_supervisor_save"),
    path('addstudent',hodviews.AddStudent,name="addstudent"),
    path('add_student_save',hodviews.Add_Student_Save,name="add_student_save"),
    path('manage_student',hodviews.Manage_Student,name="manage_student"),
    path('edit_student/<str:student_id>',hodviews.Edit_Student,name="edit_student"),
    path('edit_student_save', hodviews.Edit_Student_Save, name="edit_student_save"),
    path('adddepartment',hodviews.AddDepartment,name="adddepartment"),
    path('department_save',hodviews.Department_Save,name="department_save"),
    path('manage_department',hodviews.Manage_Department,name="manage_department"),
    path('edit_department/<str:department_id>',hodviews.Edit_Department,name="edit_department"),
    path('edit_department_save',hodviews.Edit_Department_Save,name="edit_department_save"),
    path('currentfyp',hodviews.CurrentFyp,name="currentfyp"),
    path('add_fyp', hodviews.Add_Fyp, name="add_fyp"),
    path('fyp_save',hodviews.Fyp_Save,name="fyp_save"),
    path('pastfyp',hodviews.PastFyp,name="pastfyp"),
    path('uploadreport',hodviews.UploadReport,name="uploadreport"),
    path('logout',hodviews.LogOut,name='logout'),
    path('show_profile',hodviews.Show_Profile,name="show_profile"),
    path('upload_report',hodviews.UploadReport,name="upload_report"),
    path('n_gram',hodviews.N_Gram,name="n_gram"),
    path('downloadd/<str:pathh>', hodviews.Downloadd, name="downloadd"),
    path('admin/', admin.site.urls),
    #Department Admin Urls
    path('base_class_admin_dep',dep_admin_views.BaseClass,name="base_class_admin_dep"),
    path('add_supervisor',dep_admin_views.AddSupervisor,name="add_supervisor"),
    path('supervisor_savee', dep_admin_views.Add_Supervisor_Save, name="supervisor_savee"),
    path('managee_supervisor',dep_admin_views.Manage_Supervisor,name="managee_supervisor"),
    path('edit_supervisors/<str:supervisors_id>',dep_admin_views.Edit_Supervisors,name='edit_supervisors'),
    path('edit_save_supervisors',dep_admin_views.Edit_Save_Supervisors,name="edit_save_supervisors"),
    path('add_student',dep_admin_views.Add_Student,name="add_student"),
    path('add_student_savee',dep_admin_views.Add_Student_Savee,name="add_student_savee"),
    path('manage_students',dep_admin_views.Manage_Students,name="manage_students"),
    path('edit_students/<str:student_id>',dep_admin_views.Edit_Students,name="edit_students"),
    path('edit_students_save',dep_admin_views.Edit_Students_Save,name="edit_students_save"),
    path('fyp_addd', dep_admin_views.Fyp_Add, name="fyp_addd"),
    path('fyp_saved', dep_admin_views.Fyp_Savee, name="fyp_saved"),
    path('past_fyp',dep_admin_views.Past_Fyp,name="past_fyp"),
    path('showprofile', dep_admin_views.Show_Profile, name="showprofile"),
    path('check_plag', dep_admin_views.Check_plagiarism, name="check_plag"),
    path('Logout_a', dep_admin_views.Logout, name="Logout_a"),
     #Supervisors
    path('base_class_supervisor',supervisors_views.BaseClass,name="base_class_supervisor"),
    path('fyp_added',supervisors_views.Show_Fyp,name="fyp_added"),
    path('save_fypp',supervisors_views.Save_FYP,name="save_fypp"),
    path('fyp_list',supervisors_views.Display_Fyp,name="fyp_list"),
    path('upload_reps',supervisors_views.Upload_Reports,name="upload_reps"),
    path('upload_plag',supervisors_views.Upload_Plag,name="upload_plag"),
    path('profile_sup',supervisors_views.Profile_Supervisor,name="profile_sup"),
    path('logout_sup',supervisors_views.LogOut,name="logout_sup"),

    #Student Views
    path('base_class_student',student_views.BaseClass,name="base_class_student"),
    path('add_fyp_s',student_views.AddFyp,name="add_fyp_s"),
    path('fyp_s_save',student_views.Fyp_s_Save,name="fyp_s_save"),
    path('past_fyp_s',student_views.PastFyp,name="past_fyp_s"),
    path('upload_report_s',student_views.UploadReport,name="upload_report_s"),
    path('show_profiles', student_views.ShowProfile, name="show_profiles"),
    path('Logout_stud', student_views.LogOUt, name="Logout_stud"),
    path('plag_stud', student_views.Plag_Student, name="plag_stud"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
#print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))