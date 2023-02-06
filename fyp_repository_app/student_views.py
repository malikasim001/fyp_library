from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from fyp_repository_app.models import CustomUser, Departments, Projects

#login addfyp past fyp uploadreport see profile logout
def BaseClass(request):
    return render(request,"student_templates/base_class.html")

def AddFyp(request):
    departments = Departments.objects.all()
    supervisors = CustomUser.objects.filter(user_type=2)
    return render(request,"student_templates/addfyp.html", {"departments": departments, "supervisors": supervisors})
    # return HttpResponse("HELLO")
def Fyp_s_Save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        title = request.POST.get("pro_title")
        year = request.POST.get("year")
        sup_id=request.POST.get("sup_id")
        dep_id=request.POST.get("dep_id")
        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)
        try:
            department_model = Projects(title=title,year=year,dep_id_id=dep_id,admin_id=sup_id,report_file=profile_pic_url)
            department_model.save()
            return HttpResponseRedirect("/add_fyp_s")
        # p=Projects.objects.get(title=title)
        # return HttpResponse(department_model)
        except:
            return HttpResponse("FAILED TO ADD FYP")

def PastFyp(request):
    project = Projects.objects.all()
    return render(request,"student_templates/pastfyp.html", {"projects":project})
    #return HttpResponse("HELLO")

def UploadReport(request):
    return render(request,"student_templates/uploadreport.html")
    #return HttpResponse("HELLO")

def ShowProfile(request):
    user = CustomUser.objects.get(id=request.user.id)
    return render(request, "student_templates/show_profile.html", {"user": user})
    #return HttpResponse("HEllo")

def LogOUt(request):
    logout(request)
    return HttpResponseRedirect("/")