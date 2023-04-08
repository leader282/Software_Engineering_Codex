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
    if tempc_admin.cadmin.c_profile in ['s', 'd', 'f', 'q']:
        tempc_admin.cadmin.c_profile = PROFILE_CHOICES[tempc_admin.cadmin.c_profile]

    if request.method == 'POST':
        try:
            if request.POST['hire'] == 'T':
                if tempc_admin.cadmin.ishiring:
                    tempc_admin.cadmin.ishiring = False
                else:
                    tempc_admin.cadmin.ishiring = True
                tempc_admin.save()
                tempc_admin.cadmin.save()
        except:
            pass
        
        try:
            file = request.FILES['cert']
            tempc_admin.cadmin.cert = file
            tempc_admin.save()
            tempc_admin.cadmin.save()
        except:
            pass

        try:
            email = request.POST['email']
            tempc_admin.cadmin.c_email = email
            tempc_admin.save()
            tempc_admin.cadmin.save()
        except:
            pass

        try:
            phone = request.POST['phone']
            tempc_admin.cadmin.c_contactno = phone
            tempc_admin.save()
            tempc_admin.cadmin.save()
        except:
            pass

        try:
            about = request.POST['c_about']
            print(about)
            tempc_admin.cadmin.about = about
            tempc_admin.save()
            tempc_admin.cadmin.save()
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print (message)

        try:
            photo = request.FILES['photo']
            tempc_admin.cadmin.photo = photo
            tempc_admin.save()
            tempc_admin.cadmin.save()
        except:
            pass

    photo = tempc_admin.cadmin.photo

    try:
        img_path = os.path.join(settings.BASE_DIR, '/media/')+photo.name
    except:
        img_path = ""

    context = {
        'cadmin' : tempc_admin,
        'cv_path' : os.path.join(settings.BASE_DIR, '/media/'),
        'img_path' : img_path,
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

        if(password != cpassword):
            return render(request, "cadmin/register.html", context={'e2' : True})

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
            return render(request, 'cadmin/login.html', context={'e1' : True})

    return render(request, "cadmin/login.html")

def logout_view(request):
    logout(request)
    return redirect('/')