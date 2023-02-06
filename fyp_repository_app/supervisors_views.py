from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from fyp_repository_app.models import CustomUser, Departments, Projects


# logout view profile add fyp past fyp  upload report
def BaseClass(request):
    return render(request,"supervisor_templates/base_class.html")

def Show_Fyp(request):
    departments = Departments.objects.all()
    supervisors = CustomUser.objects.filter(user_type=2)
    return render(request, "supervisor_templates/add_fyp.html", {"departments": departments, "supervisors": supervisors})
    return HttpResponse("HELLO")

def Save_FYP(request):
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
            return HttpResponseRedirect("/fyp_added")
        # p=Projects.objects.get(title=title)
        # return HttpResponse(department_model)
        except:
            return HttpResponse("FAILED TO ADD FYP")

def Display_Fyp(request):
    project = Projects.objects.all()
    return render(request, "supervisor_templates/past_fyp.html", {"projects": project})

def Upload_Plag(request):
    return HttpResponse("HELLO")

def Profile_Supervisor(request):
    user = CustomUser.objects.get(id=request.user.id)
    return render(request, "supervisor_templates/show_profile.html", {"user": user})


def LogOut(request):
    logout(request)
    return HttpResponseRedirect("/")