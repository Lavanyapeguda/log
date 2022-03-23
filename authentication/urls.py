from django.contrib import admin
from django.conf.urls import url,include
from authentication import views

urlpatterns=[

    url(r'HOSPITAL/',views.HOSPITAL),
    url(r'^home/',views.Home,name="home"),
    url(r'^signup/',views.Signup,name="signup"),
    url(r'^signin/',views.Signin,name="signin"),
    url(r'^signout/',views.Signout,name="signout"),
    url(r'^phome/',views.pHome,name="phome"),
    url(r'^psignup/',views.pSignup,name="psignup"),
    url(r'^psignin/',views.pSignin,name="psignin"),
    url(r'^psignout/',views.pSignout,name="psignout"),
]