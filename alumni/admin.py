from django import forms
from django.contrib import admin

from .models import Alumni, Feedback

admin.site.register(Alumni)
admin.site.register(Feedback)