from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import District,Branch


# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('bankapp:account')
        else:
            messages.info(request, "invalid credentials")
            return redirect('bankapp:login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password== cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Already existing username")
                return redirect('bankapp:register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                messages.info(request, "user created")
                return redirect('bankapp:login')
        else:
            messages.info(request, "Password missmatch")
            return redirect('bankapp:register')
        return redirect('/')
    return render(request,'register.html')

def account(request):
    return render(request,'account.html')
def update(request):
    districts=District.objects.all()
    if request.method== 'POST':
        auth.logout(request)
        return redirect('bankapp:logout')
    return render(request,'update.html',{'districts':districts})
def logout(request):
    messages.info(request, "Application Accepted")
    return render(request,'logout.html')
def branches(request):
    district=request.GET.get('district')
    print(district)
    branches=Branch.objects.filter(district=district)
    return render(request,'partials/branches.html',{'branches':branches})