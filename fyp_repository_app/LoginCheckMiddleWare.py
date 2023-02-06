from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        user = request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "fyp_repository_app.hodviews":
                    pass
                elif modulename == "fyp_repository_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("baseclass"))
            elif user.user_type == "3":
                if modulename == "fyp_repository_app.dep_admin_views":
                    pass
                elif modulename == "fyp_repository_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("base_class_admin_dep"))
            elif user.user_type == "2":
                if modulename == "fyp_repository_app.supervisors_views":
                    pass
                elif modulename == "fyp_repository_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("base_class_supervisor"))
            elif user.user_type == "4":
                if modulename == "fyp_repository_app.student_views":
                    pass
                elif modulename == "fyp_repository_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("base_class_student"))
        else:
            if request.path == reverse("ShowLoginPage") or request.path == reverse("dologin") or modulename=="django.contrib.auth.views":
                pass
            else:
                return HttpResponseRedirect(reverse("ShowLoginPage"))


