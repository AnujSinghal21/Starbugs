from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as  auth_views

from . import views

urlpatterns =[
    path('',views.loginUser,name='loginUser'),
    path('loginUser/',views.loginUser,name='loginUser'),
    path('logoutUser/',views.logoutUser,name='logoutUser'),
    path('registerUser/',views.registerUser,name='registerUser'), 
    path('PasswordReset/',auth_views.PasswordResetView.as_view(),name='PasswordReset'),
    path('PasswordReset_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('PasswordReset_sent/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('PasswordReset_Complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]