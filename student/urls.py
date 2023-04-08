from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "student"

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('notification/', views.notif_view, name="notif"),
    path('chat', views.chat_view, name="chats"),
    path('chat/<a_id>', views.chat_view_alumni, name="chats_alumni")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)