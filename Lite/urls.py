from django.contrib import admin
from django.urls import path
from Lite import views
urlpatterns = [
    path('',views.home, name="home"),
    path('home/',views.home, name="home"),
    path('login/',views.login, name="login"),
    path('food/',views.food, name="food"),
    path('bmi_calculator/',views.bmi_calculator, name="bmi_calculator"),
    path('register/',views.register),
    path('login/',views.login),
    
]