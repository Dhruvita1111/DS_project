"""digital_society URL Configuration

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
from django.urls import path
from societymemberapp import views


urlpatterns = [
    path('',views.home, name='home'),
    path('society-profile/',views.society_profile, name='society-profile'),
    path('society-change-password/',views.society_change_password,name='society-change-password'),
    path('view-notice-society/',views.view_notice_society,name='view-notice-society'),
    path('view-notice-society-details/<int:pk>',views.view_notice_society_details,name='view-notice-society-details'),
    
    

]
