from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

def base(request):
    return render(request,"base.html")

def register(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        phonenumber=request.POST.get("phone number")
        gender=request.POST.get("gender")
        DOB=request.POST.get("DOB")
        send_mail("thanks for registration","hello {} {}\n thanks for tregistering ".format(first_name,last_name),
        "roopendrark@gmail.com",[email,],fail_silently=False)
        return HttpResponse("{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>".format(first_name,last_name,email,password,phonenumber,gender,DOB))
    return render(request,"app5/registration.html")
    
