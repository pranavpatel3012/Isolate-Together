from django.contrib import admin
from . import views
from django.urls import path,include


urlpatterns = [
    path('',include('chatrooms.urls')),
    path('',include('authentication.urls'),name="signIn"),
    path('admin', admin.site.urls),
    path('home', views.Home,name="home"),
    path('home', views.Home,name="homea"),
    path('whyIsolateTogether', views.whyIsolateTogether,name="whyIsolateTogether"),
    path('ourService_card', views.ourServiceCard),
    path('ourService', views.ourService),
    path('recoveredService', views.recoveredService),
    path('games', views.games, name="games"),
    path('EnterHospital', views.EnterHospital, name="EnterHospital"),
    path('ftrHospital', views.ftrHospital, name="ftrHospital"),
    path('postHospital', views.postHospital, name="postHospital"),
    path('homeRemedies', views.homeRemedies, name="homeRemedies"),
    path('postRemedies', views.postRemedies, name="postRemedies"),
    path('experience', views.experience, name="experience"),
    path('postExperience', views.postExperience, name="postExperience"),
    path('skills', views.skills, name="skills"),
    path('ftrskill', views.ftrskill, name="ftrskill"),
    path('ftrExp', views.ftrExp, name="ftrExp"),
    path('ftrHR', views.ftrHR, name="ftrHR"),
    path('postSkill', views.postSkill, name="postSkill"),
    path('profile',views.myProfile,name="profile"),
    path('aboutus',views.aboutus,name="aboutus"),
    path('tips',views.tips,name="tips"),
]
