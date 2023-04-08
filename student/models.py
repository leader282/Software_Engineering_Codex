from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Student(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=1000)
    email = models.EmailField(max_length=100)
    date_joined=models.DateTimeField(verbose_name="Date of Joining",auto_now_add=True, null=True) 
    phone=models.IntegerField(blank=True,null=True)
    cv_s = models.FileField(upload_to='files/', blank=True, null=True)
    cv_d = models.FileField(upload_to='files/', blank=True, null=True)
    cv_f = models.FileField(upload_to='files/', blank=True, null=True)
    cv_q = models.FileField(upload_to='files/', blank=True, null=True)
    photo=models.FileField(upload_to='files/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self, app_label):
        return True

class Notification(models.Model):
    text=models.CharField(max_length=10000000, default="")
    
    def __str__(self):
        return self.text[:20]