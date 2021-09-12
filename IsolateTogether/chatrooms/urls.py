from django.contrib import admin
from . import views
from django.urls import path,include


urlpatterns = [
    path('chat',views.chat,name="chat"),
    path('sendmsg',views.sendmsg),
    path('checkmsg',views.checkmsg,name="checkmsg"),
    path('getChat/', views.getChat, name="getChat"),
    path('getGroupChat/', views.getGroupChat, name="getGroupChat"),
    path('savedChats', views.savedChats, name="savedChats"),
]
