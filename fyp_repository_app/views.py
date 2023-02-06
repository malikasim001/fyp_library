import self
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from fyp_repository_app.EmailBackEnd import EmailBackEnd


# Create your views here.
def ShowLoginPage(request):
    return render(request,"loginpage.html")

def DoLogin(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        user = EmailBackEnd.authenticate(self,request, username=request.POST.get("email"),password=request.POST.get("password"))
        # user =EmailBackEnd.authenticate(self,requestusername=request.POST.get("email"),password=request.POST.get("password"))
        if user != None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect("/baseclass")
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("base_class_supervisor"))
            elif user.user_type == "3":
                return HttpResponseRedirect(reverse("base_class_admin_dep"))
            elif user.user_type == "4":
                return HttpResponseRedirect(reverse("base_class_student"))

        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")
