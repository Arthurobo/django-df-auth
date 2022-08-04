"""apex_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.urls import re_path as url 
from django.conf import settings



from social_core.utils import setting_name
from social_django import views


extra = getattr(settings, setting_name('TRAILING_SLASH'), True) and '/' or ''



urlpatterns = [
    path('admin/', admin.site.urls),
    path('social/', include('public.urls', namespace="public")),
]
