from .views import *
from django.urls import path , include
from django.contrib import admin


urlpatterns = [
    path("", main_page, name="main_page"),
    path("loginpage/",loginpage, name="loginpg"),
    path("loginact/",loginaction, name="loginaction"),
    path("list/", include('products.urls')),
    path("contacts/",contactpage,name="contacts"),
    path("dev/",devpage,name="devpage"),
    path("profile/", profile_page, name="profile_page"),
    path("register/",regpage,name="register")
    # path('admin/', admin , name="admin"),

]