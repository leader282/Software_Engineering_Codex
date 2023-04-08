from django.contrib.auth.models import User
from django.db import models
from student.models import Student

PROFILE_CHOICES = (
    ('s','SOFTWARE'),
    ('d', 'DATA'),
    ('f','FINANCE'),
    ('q','QUANT'),
)

class Alumni(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    a_name=models.CharField(max_length=1000)
    a_email = models.EmailField(max_length=100)
    date_joined=models.DateTimeField(verbose_name="Date of Joining",auto_now_add=True, null=True) 
    a_contactno=models.IntegerField(blank=True,null=True)
    a_profile=models.CharField(max_length=4, choices=PROFILE_CHOICES, default='s')
    photo=models.FileField(upload_to='files/', null=True, blank=True)

    def __str__(self):
        return self.a_name
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self, app_label):
        return True

class Chat(models.Model):
    alumni = models.ForeignKey(Alumni, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=1000000, blank=True, default="")
    isactive = models.BooleanField(default=False)

    def __str__(self):
        return self.alumni.a_name + ", " + self.student.name