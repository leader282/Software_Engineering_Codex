from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from .models import Cadmin, User


# Create your views here.

PROFILE_CHOICES = (
    ('s','SOFTWARE'),
    ('d', 'DATA'),
    ('f','FINANCE'),
    ('q','QUANT'),
)

def home(request):
    return render(request, "cadmin/index.html")

def register_view(request):
    if request.method == "POST":
        c_name = request.POST['c_name']
        c_email = request.POST['c_email']
        c_id = request.POST['c_id']
        c_contactno = request.POST['c_contactno']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        new_user = User.objects.create(username=c_id)
        new_user.set_password(password)
        new_cadmin = Cadmin.objects.create(user=new_user)
        new_cadmin.c_name = c_name
        new_cadmin.c_email = c_email
        new_cadmin.c_contactno = c_contactno
        new_user.save()
        new_cadmin.save()
        new_cadmin = authenticate(username=c_id, password=password)
        context = {
            'cadmin' : new_user,
        }
        return render(request, "cadmin/index.html", context=context)

    return render(request, "cadmin/register.html", context={"choices" : PROFILE_CHOICES})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['c_id']
        password = request.POST['password']

        cadmin = authenticate(username=username, password=password)
        context = {
            'cadmin' : cadmin,
        }

        if cadmin is not None:
            return render(request, "cadmin/index.html", context=context)
        else:
            return redirect('/cadmin/login')

    return render(request, "cadmin/login.html")

def logout_view(request):
    logout(request)
    return redirect('/cadmin')