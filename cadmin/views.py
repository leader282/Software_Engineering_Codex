from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from .models import Cadmin, User
from student.models import Student
from django.conf import settings
import os


# Create your views here.

PROFILE_CHOICES = {'s':'SOFTWARE', 'd': 'DATA', 'f':'FINANCE', 'q':'QUANT'}

def home(request):
    cadmin = User.objects.filter(username=request.session['username'])[0]
          
    student_list = cadmin.cadmin.students.all()

    tempc_admin = cadmin
    tempc_admin.cadmin.c_profile = PROFILE_CHOICES[tempc_admin.cadmin.c_profile]

    context = {
        'cadmin' : tempc_admin,
        'cv_path' : os.path.join(settings.BASE_DIR, '/media/'),
        'student_list' : student_list
    }
    return render(request, "cadmin/index.html", context=context)

def register_view(request):
    if request.method == "POST":
        c_name = request.POST['c_name']
        c_email = request.POST['c_email']
        c_id = request.POST['c_id']
        c_contactno = request.POST['c_contactno']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        c_profile = request.POST['c_profile']

        new_user = User.objects.create(username=c_id)
        new_user.set_password(password)
        new_cadmin = Cadmin.objects.create(user=new_user)
        new_cadmin.c_name = c_name
        new_cadmin.c_email = c_email
        new_cadmin.c_contactno = c_contactno
        new_cadmin.c_profile = c_profile
        new_user.save()
        new_cadmin.save()
        new_cadmin = authenticate(username=c_id, password=password)
        request.session['username'] = c_id
        return redirect('/cadmin')

    return render(request, "cadmin/register.html", context={"choices" : PROFILE_CHOICES})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['c_id']
        password = request.POST['password']

        cadmin = authenticate(username=username, password=password)

        if cadmin is not None:
            request.session['username'] = username
            return redirect('/cadmin')
        else:
            return redirect('/cadmin/login')

    return render(request, "cadmin/login.html")

def logout_view(request):
    logout(request)
    return redirect('/')