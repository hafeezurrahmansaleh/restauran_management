from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='user_login'),
    path('signup/', views.signup, name='user_signup'),
    path('calculator/', views.calculator, name='calculator'),
]
