"""
URL configuration for tut1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('about', views.pipe1, name='index0'),
    path('pipe1', views.pipe2, name='index1'),
    path('pipe2', views.pipe3, name='index2'),
    path('textutils', include('textutils.urls')),
    path('portfolio', include('portfolio.urls')),
    path('ecommerce', include('eccomerce.urls'))
]
