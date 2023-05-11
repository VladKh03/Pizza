"""
URL configuration for Pizza project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

from service import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('first/', views.first, name='first'),
    path('second/', views.second, name='second'),
    path('third/', views.third, name='third'),
    path('fourth/', views.fourth, name='fourth'),
    path('fifth/', views.fifth, name='fifth'),
    path('sixth/', views.sixth, name='sixth'),
    path('seventh/', views.seventh, name='seventh'),
    path('eighth/', views.eighth, name='eighth'),
    path('ninth/', views.ninth, name='ninth'),
]
