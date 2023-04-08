from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from .models import Student, User
from cadmin.models import Cadmin
from alumni.models import Alumni, Chat
from django.conf import settings
import os

PROFILE_CHOICES = {'s':'SOFTWARE', 'd': 'DATA', 'f':'FINANCE', 'q':'QUANT'}

# Create your views here.

def home(request):
    try:
        student = User.objects.filter(username=request.session['username'])[0]

        if request.method == 'POST':
            try:
                cv = request.FILES['cv_s']
                student.student.cv_s = cv
                student.save()
                student.student.save()
            except:
                pass

            try:
                cv = request.FILES['cv_q']
                student.student.cv_q = cv
                student.save()
                student.student.save()
            except:
                pass

            try:
                cv = request.FILES['cv_d']
                student.student.cv_d = cv
                student.save()
                student.student.save()
            except:
                pass

            try:
                cv = request.FILES['cv_f']
                student.student.cv_f = cv
                student.save()
                student.student.save()
            except:
                pass

            try:
                photo = request.FILES['photo']
                student.student.photo = photo
                student.save()
                student.student.save()
            except:
                pass

            try:
                c_apply = request.POST['c_apply']
                company = Cadmin.objects.filter(c_name = c_apply)[0]
                company.students.add(student.student)
                company.save()
            except:
                pass

            try:
                alumni = request.POST['a_apply']
                user = User.objects.filter(username=alumni)[0]
                alumni = Alumni.objects.filter(user=user)[0]
                chats = Chat.objects.filter(alumni=alumni, student=student.student)
                if(len(chats) == 0):
                    Chat.objects.create(student=student.student, alumni=alumni, text="")
            except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                print (message)

            try:
                email = request.POST['email']
                student.student.email = email
                student.save()
                student.student.save()
            except:
                pass

            try:
                phone = request.POST['phone']
                student.student.phone = phone
                student.save()
                student.student.save()
            except:
                pass
            
        company_list = Cadmin.objects.filter(isverified=True)
        for company in company_list:
            if company.c_profile in PROFILE_CHOICES:
                company.c_profile = PROFILE_CHOICES[company.c_profile]

        alumni_list = Alumni.objects.all()
        for alumni in alumni_list:
            if alumni.a_profile in PROFILE_CHOICES:
                alumni.a_profile = PROFILE_CHOICES[alumni.a_profile]

        photo = student.student.photo

        try:
            img_path = os.path.join(settings.BASE_DIR, '/media/')+photo.name
        except:
            img_path = ""

        context = {
            'student' : student,
            'img_path' : img_path,
            'gen_path' : os.path.join(settings.BASE_DIR, '/media/'),
            'company_list' : company_list,
            'alumni_list' : alumni_list,
        }
        return render(request, "student/index.html", context=context)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print (message)
        return render(request, "student/index.html")

def register_view(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        roll = request.POST['roll']
        phone = request.POST['phone']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if(password != cpassword):
            return render(request, "student/register.html", context={'e2' : True})

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

def notif_view(request):
    student = User.objects.filter(username=request.session['username'])[0]
    company_list = Cadmin.objects.all()

    context = {
        'student': student,
        'company_list': company_list
    }

    return render(request, "student/notification.html", context=context)

def chat_view(request):
    student = User.objects.filter(username=request.session['username'])[0]
    chat_list = Chat.objects.filter(student=student.student)

    for chat in chat_list:
        if chat.alumni.a_profile in PROFILE_CHOICES:
            chat.alumni.a_profile = PROFILE_CHOICES[chat.alumni.a_profile]
    
    context = {
        'chat_list' : chat_list,
        'student': student,
        'cv_path' : os.path.join(settings.BASE_DIR, '/media/'),
    }

    return render(request, "student/chat.html", context=context)

def chat_view_alumni(request, a_id):
    student = User.objects.filter(username=request.session['username'])[0]
    alumni = User.objects.filter(username=a_id)[0]
    chat = Chat.objects.filter(student=student.student, alumni=alumni.alumni)[0]
    if request.method == 'POST':
        text = request.POST['chat_stu']
        text = text + '\s+'
        chat.text = chat.text + text
        chat.save()

    txt_list = chat.text.split('+')[0:-1]
    
    context = {
        'txt_list': txt_list,
        'student': student,
        'alumni': alumni,
        'cv_path' : os.path.join(settings.BASE_DIR, '/media/'),
    }

    return render(request, "student/chat_u.html", context=context)