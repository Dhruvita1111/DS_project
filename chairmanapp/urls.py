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
from chairmanapp import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('logout/',views.logout, name='logout'),
    path('chairman-profile/',views.chairman_profile, name='chairman-profile'),
    path('chairman-change-password/',views.chairman_change_password,name='chairman-change-password'),
    path('add-member/',views.add_member,name='add-member'),
    path('add-notice/',views.add_notice,name='add-notice'),
    path('view-notice/',views.view_notice,name='view-notice'),
    path('view-notice-details/<int:pk>',views.view_notice_details,name='view-notice-details'),
    path('all-societymembers/',views.all_societymembers, name='all-societymembers'),
    path('societyspecification-profile/<int:pk>',views.societyspecification_profile, name='societyspecification-profile'),
    path('forgot-password/',views.forgot_password, name='forgot-password'),
    path('change-password/',views.change_password_value, name='change-password-value'),
    path('add-maintainance/',views.add_maintainance, name='add-maintainance'),
    path('all-maintainance/',views.all_maintainance, name='all-maintainance'),
    path('add-event/',views.add_event,name='add-event'),
    path('view-event/',views.view_event,name='view-event'),
    path('view-event-details/<int:pk>',views.view_event_details,name='view-event-details'),
    path('add-complain/',views.add_complain,name='add-complain'),
    path('view-complain/',views.view_complain,name='view-complain'),
    path('view-complain-details/<int:pk>',views.view_complain_details,name='view-complain-details'),
    path('register/',views.register,name='register'),


]
