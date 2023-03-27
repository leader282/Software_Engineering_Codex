from django.urls import path
from . import views

app_name = "cadmin"

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout")
]