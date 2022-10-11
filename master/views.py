from django.shortcuts import redirect, render
from .models import *

class Master:
    # def persson(request):
    #     list=["Master","Sub Master","Nursery","Manager","Marketing","Customer"]
    #     for i in list:
    #         Person.objects.create(person=i,status=True)
    #     return render(request,"home.html")
    def user_register(request):
        level=Person.objects.filter(id__in=[2,3,4,5,6])
        if request.method=="POST":
            register_mobile=Register.objects.filter(mobile=request.POST["mobile"])
            register_email=Register.objects.filter(email=request.POST["email"])            
            if register_mobile:
                return render(request,"login.html",{"msg":"Mobile Number Alredy Registerd"})
            elif register_email:
                return render(request,"login.html",{"msg":"Email Alredy Registerd"})
            else:
                Register.objects.create(
                status=True,
                user_id="",
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                email=request.POST["email"],
                mobile=request.POST["mobile"],
                create_by_id=7,
                password="",
                gender_id=4
                )
                return redirect("login")
        return render(request,"register.html",{"person_level":level})
    def login(request):
        
        return render(request,"login.html",{})
    def home(request):
        return render(request,"home.html",{})
    def view(request):

        return render(request,"view.html",{})