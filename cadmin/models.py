from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from student.models import Student

PROFILE_CHOICES = (
    ('s','SOFTWARE'),
    ('d', 'DATA'),
    ('f','FINANCE'),
    ('q','QUANT'),
)

class Cadmin(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    students = models.ManyToManyField(Student, blank=True)
    c_name=models.CharField(max_length=1000)
    c_email = models.EmailField(max_length=100)
    date_joined=models.DateTimeField(verbose_name="Date of Joining",auto_now_add=True, null=True) 
    c_contactno=models.IntegerField(blank=True,null=True)
    c_profile=models.CharField(max_length=4, choices=PROFILE_CHOICES, default='s')
    ishiring=models.BooleanField(default=False)
    isverified=models.BooleanField(default=False)
    cert = models.FileField(upload_to='files/', null=True, blank=True)
    about=models.TextField(blank=True)
    photo=models.FileField(upload_to='files/', null=True, blank=True)

    def __str__(self):
        return self.c_name
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self, app_label):
        return True