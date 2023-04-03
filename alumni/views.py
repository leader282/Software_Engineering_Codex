from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from .models import Alumni, User
from student.models import Student
from django.conf import settings
import os

# Create your views here.

PROFILE_CHOICES = {'s':'SOFTWARE', 'd': 'DATA', 'f':'FINANCE', 'q':'QUANT'}

def home(request):
    try:
        alumni = User.objects.filter(username=request.session['username'])[0]
            
        student_list = Student.objects.all()

        temp_alumni = alumni
        temp_alumni.alumni.a_profile = PROFILE_CHOICES[temp_alumni.alumni.a_profile]

        context = {
            'alumni' : temp_alumni,
            'cv_path' : os.path.join(settings.BASE_DIR, '/media/'),
            'student_list' : student_list
        }
        return render(request, "alumni/index.html", context=context)
    except:
        return render(request, "alumni/index.html")

def register_view(request):
    if request.method == "POST":
        a_name = request.POST['a_name']
        a_email = request.POST['a_email']
        a_id = request.POST['a_id']
        a_contactno = request.POST['a_contactno']
        password = request.POST['password']
        apassword = request.POST['apassword']
        a_profile = request.POST['a_profile']

        new_user = User.objects.create(username=a_id)
        new_user.set_password(password)
        new_alumni = Alumni.objects.create(user=new_user)
        new_alumni.a_name = a_name
        new_alumni.a_email = a_email
        new_alumni.a_contactno = a_contactno
        new_alumni.a_profile = a_profile
        new_user.save()
        new_alumni.save()
        new_alumni = authenticate(username=a_id, password=password)
        request.session['username'] = a_id
        return redirect('/alumni')

    return render(request, "alumni/register.html", context={"choices" : PROFILE_CHOICES})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['a_id']
        password = request.POST['password']

        alumni = authenticate(username=username, password=password)

        if alumni is not None:
            request.session['username'] = username
            return redirect('/alumni')
        else:
            return redirect('/alumni/login')

    return render(request, "alumni/login.html")

def logout_view(request):
    logout(request)
    return redirect('/')