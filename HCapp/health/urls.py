from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('submitdate',views.submitdate,name='submitdate'),
    path('submitfinal',views.submitfinal,name='submitfinal'),
    path('book_appointment/',views.book_appointment,name='book_appointment'),
    path('show_appointments/',views.show_appointments,name='show_appointments'),
    
]