from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns =[
    path('loginUser',views.loginUser,name='loginUser'),
    path('logoutUser',views.logoutUser,name='logoutUser'),
    path('registerUser',views.registerUser,name='registerUser'),  
]