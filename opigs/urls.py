"""opigs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, reverse_lazy
from django.views.generic.base import RedirectView
from . import views

app_name = "opigs"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('student.urls')),
    path('cadmin/', include('cadmin.urls')),
    path('iadmin/', include('iadmin.urls')),
    path('alumni/', include('alumni.urls')),
    path('', views.home, name="home"),
]

admin.site.site_header  =  "Institute Admin"  
admin.site.site_title  =  "Online Placement Information Gathering System | Institute Admin"
admin.site.index_title  =  "Institute Admin"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)