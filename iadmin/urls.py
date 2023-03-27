from django.urls import path
from . import views

app_name = "iadmin"

urlpatterns = [
    path('', views.home, name="home")
]
