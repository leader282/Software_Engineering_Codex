from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from .models import Student, User


# Create your views here.

def home(request):
    return render(request, "student/index.html")

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
        context = {
            'student' : new_user,
        }
        return render(request, "student/index.html", context=context)

    return render(request, "student/register.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['roll']
        password = request.POST['password']

        student = authenticate(username=username, password=password)
        context = {
            'student' : student,
        }

        if student is not None:
            return render(request, "student/index.html", context=context)
        else:
            return redirect('/students/login')

    return render(request, "student/login.html")

def logout_view(request):
    logout(request)
    return redirect('/students')