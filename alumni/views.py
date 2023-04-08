from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from .models import Alumni, User, Chat
from student.models import Student
from django.conf import settings
import os

# Create your views here.

PROFILE_CHOICES = {'s':'SOFTWARE', 'd': 'DATA', 'f':'FINANCE', 'q':'QUANT'}

def home(request):
    try:
        alumni = User.objects.filter(username=request.session['username'])[0]
            
        student_list = Student.objects.all()

        if alumni.alumni.a_profile in PROFILE_CHOICES:
            alumni.alumni.a_profile = PROFILE_CHOICES[alumni.alumni.a_profile]

        if request.method == 'POST':
            try:
                photo = request.FILES['photo']
                alumni.alumni.photo = photo
                alumni.save()
                alumni.alumni.save()
            except:
                pass

            try:
                email = request.POST['email']
                alumni.alumni.a_email = email
                alumni.save()
                alumni.alumni.save()
            except:
                pass

            try:
                phone = request.POST['phone']
                alumni.alumni.a_contactno = phone
                alumni.save()
                alumni.alumni.save()
            except:
                pass

        context = {
            'alumni' : alumni,
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

def chat_view(request):
    alumni = User.objects.filter(username=request.session['username'])[0]
    chat_list = Chat.objects.filter(alumni=alumni.alumni)

    if request.method == 'POST':
        chat = request.POST['chat_approve']
        roll=chat
        user = User.objects.filter(username=roll)[0]
        student = Student.objects.filter(user=user)[0]
        chat = Chat.objects.filter(student=student)[0]
        chat.isactive = True
        chat.save()
    
    context = {
        'chat_list' : chat_list,
        'cv_path' : os.path.join(settings.BASE_DIR, '/media/'),
        'alumni': alumni
    }

    return render(request, "alumni/chat.html", context=context)

def chat_view_student(request, s_id):
    alumni = User.objects.filter(username=request.session['username'])[0]
    student = User.objects.filter(username=s_id)[0]
    chat = Chat.objects.filter(student=student.student, alumni=alumni.alumni)[0]
    if request.method == 'POST':
        text = request.POST['chat_alu']
        text = text + '\l+'
        chat.text = chat.text + text
        chat.save()

    txt_list = chat.text.split('+')[0:-1]
    
    context = {
        'txt_list': txt_list,
        'alumni': alumni,
        'student': student,
        'cv_path' : os.path.join(settings.BASE_DIR, '/media/'),
    }

    return render(request, "alumni/chat_u.html", context=context)