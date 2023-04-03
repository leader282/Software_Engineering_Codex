from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from .models import Student, User
from cadmin.models import Cadmin
from alumni.models import Alumni, Feedback
from django.conf import settings
import os

PROFILE_CHOICES = {'s':'SOFTWARE', 'd': 'DATA', 'f':'FINANCE', 'q':'QUANT'}

# Create your views here.

def home(request):
    student = User.objects.filter(username=request.session['username'])[0]

    if request.method == 'POST':
        if len(request.FILES) > 0:
            cv = request.FILES['cv']
            student.student.cv = cv
            student.save()
            student.student.save()
        try:
            c_apply = request.POST['c_apply']
            company = Cadmin.objects.filter(c_name = c_apply)[0]
            company.students.add(student.student)
            company.save()
        except:
            pass
        try:
            alumni = request.POST['a_apply']
            print(alumni.a_name)
        except:
            pass
          
    company_list = Cadmin.objects.all()
    for company in company_list:
        company.c_profile = PROFILE_CHOICES[company.c_profile]

    alumni_list = Alumni.objects.all()
    for alumni in alumni_list:
        alumni.a_profile = PROFILE_CHOICES[alumni.a_profile]

    try:
        feedback = Feedback.objects.filter(student=student.student)[0]
    except:
        feedback = ""

    cv = student.student.cv

    context = {
        'student' : student,
        'cv_path' : os.path.join(settings.BASE_DIR, '/media/')+cv.name,
        'company_list' : company_list,
        'alumni_list' : alumni_list,
        'feedback' : feedback
    }
    return render(request, "student/index.html", context=context)

def register_view(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        roll = request.POST['roll']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        new_user = User.objects.create(username=roll)
        new_user.set_password(password)
        new_student = Student.objects.create(user=new_user)
        new_student.name = name
        new_student.email = email
        new_student.phone = phone
        new_user.save()
        new_student.save()
        new_user = authenticate(username=roll, password=password)
        request.session['username'] = roll
        return redirect('/students')

    return render(request, "student/register.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['roll']
        password = request.POST['password']

        student = authenticate(username=username, password=password)

        if student is not None:
            request.session['username'] = username
            return redirect('/students')
        else:
            return redirect('/students/login')

    return render(request, "student/login.html")

def logout_view(request):
    logout(request)
    return redirect('/')