"""blog URL Configuration

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
from .import views
urlpatterns = [
     path('',views.index),
     path('search',views.search),
     path('search_action',views.search_action,name="search_action"),
     path('signup',views.signup,name="signup"),
     path('signup-action',views.signup_action,name="signup_action"),
     path('signin',views.signin,name="signin"),
     path('signin-action',views.signin_action,name="signin_action"),



]
