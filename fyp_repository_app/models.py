from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class CustomUser(AbstractUser):
    user_type_data=((1,"HOD"),(2,"supervisor"),(3,"admindep"),(4,"Student"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Departments(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Admindep(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    address=models.CharField(max_length=255)
    gender=models.CharField(max_length=255,default="")
    profile_pic=models.FileField(default="")
    office_location=models.CharField(max_length=255,default="")
    dep_id=models.ForeignKey(Departments,on_delete=models.CASCADE,default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Supervisor(models.Model):
    id=models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address=models.TextField()
    gender = models.CharField(max_length=20,default="")
    profile_pic = models.FileField(default="")
    office_location=models.CharField(max_length=255,default="")
    designation=models.CharField(max_length=255,default="")
    dep_id = models.ForeignKey(Departments, on_delete=models.CASCADE,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    year = models.DateField(default=2020)
    dep_id=models.ForeignKey(Departments,on_delete=models.CASCADE,default=1)
    admin=models.ForeignKey(CustomUser, on_delete=models.CASCADE,default=1)
    report_file = models.FileField(default='none')
    # admin = models.OneToManyField(CustomUser, on_delete=models.CASCADE)
    objects = models.Manager()

class Student(models.Model):
    id=models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address=models.TextField()
    gender = models.CharField(max_length=20,default="")
    profile_pic = models.FileField(default="")
    cgpa=models.CharField(max_length=4,default="")
    dep_id=models.ForeignKey(Departments,on_delete=models.CASCADE,default=1)
    #project_id=models.ForeignKey(Projects,on_delete=models.CASCADE,default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            Supervisor.objects.create(admin=instance)
        if instance.user_type==3:
            Admindep.objects.create(admin=instance)
        if instance.user_type==4:
            Student.objects.create(admin=instance)
@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.supervisor.save()
    if instance.user_type==3:
        instance.admindep.save()
    if instance.user_type==4:
        instance.student.save()
