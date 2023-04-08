from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Student, Notification

admin.site.register(Student)
admin.site.unregister(Group)
admin.site.register(Notification)