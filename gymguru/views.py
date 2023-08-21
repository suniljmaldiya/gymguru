from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login




def home_page(request):
    return render(request,"index.html")
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.full_name = full_name
        myuser.save()
        
        messages.success(request,"Congrulations !!! Your account has been successfully created")
        return redirect('loginus')

    return render(request,"register.html")
def loginus(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            auth_login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,"Bad credentials")
            return redirect('loginus')

    return render(request,"loginus.html")

def logoutus(request):
    logout(request)
    messages.success(request,'You are successfully logout')
    return redirect('home')
def dashboard(request):
    return render(request,"dashboard.html")
def contact(request):
    return render(request,"contact.html")
def faq(request):
    return render(request,"faq.html")

