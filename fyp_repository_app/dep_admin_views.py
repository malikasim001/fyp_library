from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from fyp_repository_app.models import Departments, CustomUser, Admindep, Supervisor, Student, Projects


def BaseClass(request):
    user = CustomUser.objects.get(id=request.user.id)
    return render(request,"simple_admin/admin_base_class.html",{"user":user})

def AddSupervisor(request):
    departments = Departments.objects.all()
    return render(request, "simple_admin/add_supervisor.html",{"departments":departments})

def Add_Supervisor_Save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        office_loc = request.POST.get("office_loc")
        designation = request.POST.get("designation")
        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)
        dep_id = request.POST.get("dep_id")
        try:
            user = CustomUser.objects.create_user(username=username, email=email, password=password,
                                                  last_name=last_name, first_name=first_name, user_type=2)
            user.supervisor.address = address
            user.supervisor.gender = gender
            user.supervisor.office_location = office_loc
            user.supervisor.designation = designation
            user.supervisor.profile_pic = profile_pic_url
            dep_obj = Departments.objects.get(id=dep_id)
            user.supervisor.dep_id = dep_obj
            user.save()
            return HttpResponseRedirect("/add_supervisor")
        except:
            return HttpResponse("Failed to add SuperVisor")

def Manage_Supervisor(request):
    user = CustomUser.objects.get(id=request.user.id)
    depp_id = user.admindep.dep_id
    supervisors = Supervisor.objects.filter(dep_id=depp_id)
    return render(request, "simple_admin/manage_supervisor.html",{"supervisorss":supervisors})
    #return HttpResponse("Hello")

def Edit_Supervisors(request,supervisors_id):
    departments = Departments.objects.all()
    supervisor = Supervisor.objects.get(admin=supervisors_id)
    return render(request, "simple_admin/edit_supervisor.html", {"admins": supervisor,"departments": departments})

def Edit_Save_Supervisors(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        supervisor_id = request.POST.get("supervisor_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        office_loc = request.POST.get("office_loc")
        designation=request.POST.get("designation")
        dep_id = request.POST.get("dep_id")
        # if request.FILES['profile_pic']:
        if request.FILES.get('profile_pic', False):
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None

        try:
            user = CustomUser.objects.get(id=supervisor_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()
            supervisor = Supervisor.objects.get(admin=supervisor_id)
            supervisor.address = address
            supervisor.gender = gender
            supervisor.office_location = office_loc
            department = Departments.objects.get(id=dep_id)
            supervisor.dep_id = department
            if profile_pic_url != None:
                supervisor.profile_pic = profile_pic_url

            supervisor.save()
            return HttpResponseRedirect("/managee_supervisor")

        except:
            return HttpResponse("Failed to update Supervisor")


def Add_Student(request):
    departments = Departments.objects.all()
    supervisors = CustomUser.objects.filter(user_type='2')
    return render(request, "simple_admin/add_student.html", {"departments": departments, "supervisors": supervisors})

def Add_Student_Savee(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        cgpa=request.POST.get("cgpa")
        gender=request.POST.get("gender")
        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)
        dep_id = request.POST.get("dep_id")
        try:
            user = CustomUser.objects.create_user(username=username, email=email, password=password,
                                                  last_name=last_name, first_name=first_name, user_type=4)
            user.student.address=address
            user.student.gender=gender
            user.student.cgpa=cgpa
            user.student.profile_pic = profile_pic_url
            dep_obj = Departments.objects.get(id=dep_id)
            user.student.dep_id = dep_obj
            user.save()
            return HttpResponseRedirect("/add_student")
        except:
            return HttpResponse("Failed to add student")

def Manage_Students(request):
    user=CustomUser.objects.get(id=request.user.id)
    depp_id=user.admindep.dep_id.id
    students=Student.objects.filter(dep_id=depp_id)
    return render(request, "simple_admin/manage_students.html",{"students": students})

def Edit_Students(request,student_id):
    departments = Departments.objects.all()
    students = Student.objects.get(admin=student_id)
    return render(request, "simple_admin/edit_students.html", {"students": students, "departments": departments})

def Edit_Students_Save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        if request.method != "POST":
            return HttpResponse("Method Not Allowed")
        else:
            student_id = request.POST.get("student_id")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            address = request.POST.get("address")
            gender = request.POST.get("gender")
            cgpa = request.POST.get("cgpa")
            dep_id = request.POST.get("dep_id")
            # if request.FILES['profile_pic']:
            if request.FILES.get('profile_pic', False):
                profile_pic = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
            else:
                profile_pic_url = None

            try:
                user = CustomUser.objects.get(id=student_id)
                user.first_name = first_name
                user.last_name = last_name
                user.username = username
                user.email = email
                user.save()
                students = Student.objects.get(admin=student_id)
                students.address = address
                students.gender = gender
                students.cgpa = cgpa
                department = Departments.objects.get(id=dep_id)
                students.dep_id = department
                if profile_pic_url != None:
                    students.profile_pic = profile_pic_url
                students.save()
                return HttpResponseRedirect("/manage_students")

            except:
                return HttpResponse("Failed to update Student Record")


def Fyp_Add(request):
    departments = Departments.objects.all()
    supervisors = CustomUser.objects.filter(user_type=2)
    return render(request, "simple_admin/add_fyp.html", {"departments": departments, "supervisors": supervisors})

def Fyp_Savee(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        title = request.POST.get("pro_title")
        year = request.POST.get("year")
        sup_id = request.POST.get("sup_id")
        dep_id = request.POST.get("dep_id")
        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)
        try:
            department_model = Projects(title=title, year=year, dep_id_id=dep_id, admin_id=sup_id,
                                        report_file=profile_pic_url)
            department_model.save()
            return HttpResponseRedirect("/fyp_addd")
        # p=Projects.objects.get(title=title)
        # return HttpResponse(department_model)
        except:
            return HttpResponse("FAILED TO ADD FYP")

def Past_Fyp(request):
    project = Projects.objects.all()
    return render(request, "simple_admin/past_fyp.html", {"projects": project})

def Check_plagiarism(request):
    return HttpResponse("HELLO")
def Show_Profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    return render(request, "simple_admin/profile_admin.html", {"user":user})

def Logout(request):
    logout(request)
    return HttpResponseRedirect("/")