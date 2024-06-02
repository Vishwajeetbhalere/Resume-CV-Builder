from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('createcv/', views.createCv, name='createcv'),
    path('register/', views.registerView, name='reg-form'),

]
