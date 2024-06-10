from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.loginView, name="login"),
    path('logout/', views.logoutView, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('createcv/', views.createCv, name="createcv"),
    path('skill-save/', views.saveSkill, name="skill-save"),
    path('edu-save/', views.saveEducation, name="edu-save"),
    path('ref-save/', views.saveReferee, name="ref-save"),
    path('profile-save/', views.uploadProfile, name="profile-save"),
    path('register/', views.registerView, name="reg-form"),
    path('cv-detail/<id>', views.viewPDF, name="cv-detail"),
    path('cv-download/<id>', views.generate_PDF, name="cv-download"),
    path('cv-edit/', views.editCv, name="cv-edit"),

    # ^    Profile fetch,update,delete
    path('cv-edit/fetchprofile/', views.fetchProfile, name="fetchprofile"),
    path('cv-edit/updateprofile/', views.updateProfile, name="profile-update"),
    path('cv-edit/deleteprofile/', views.deleteProfile, name="profile-delete"),

    # ^   Education view, fetch, update, delete
    path('cv-edit/eduview/', views.educationView, name="edu-view"),
    path('cv-edit/eduview/academic/', views.fetchAcademic, name="fetchacademic"),
    path('cv-edit/eduview/update_academic/',
         views.updateAcademic, name="update_academic"),
    path('cv-edit/eduview/delete_academic/',
         views.deleteAcademic, name="delete_academic"),

    # ^ Skill view, fetch, update, delete
    path('cv-edit/skillview/', views.SkillView, name="skill-view"),
    path("cv-edit/skillview/skill", views.fetchSkill, name="fetchskill"),
    path('cv-edit/eduview/update_skill/',
         views.updateSkill, name="update_skill"),
    path('cv-edit/eduview/delete_academic/',
         views.deleteSkill, name="delete_skill"),

]
