from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

PROFILE_CHOICES = (
    ('s','SOFTWARE'),
    ('d', 'DATA'),
    ('f','FINANCE'),
    ('q','QUANT'),
)

class Cadmin(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    c_name=models.CharField(max_length=1000)
    c_email = models.EmailField(max_length=100)
    date_joined=models.DateTimeField(verbose_name="Date of Joining",auto_now_add=True, null=True) 
    c_contactno=models.IntegerField(blank=True,null=True)
    c_profile=models.CharField(max_length=4, choices=PROFILE_CHOICES, default='s')
    def __str__(self):
        return self.user.username
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self, app_label):
        return True