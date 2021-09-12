from django.urls import path

from . import views

urlpatterns = [
    path('signin',views.signIn,name='signIn'),
    path('postsign',views.postsign),
    path('select',views.select,name="select"),
    path('signup',views.signUp,name="signUp"),
    path('covidsignup',views.covidSignUp,name="covidSignUp"),
    path('recoveredsignup',views.recoveredSignUp,name="recoveredSignUp"),
    path('',views.logOut,name="logout"),
    path('postsignup',views.postsignup),
    path('postrecoveredsignup',views.postRecoveredSignup),
    path('registered',views.registered),
    path('enterInterest',views.enterInterest),
    path('match', views.match,name="match"),
    path('checkemail',views.checkEmail,name="checkEmail"),
]