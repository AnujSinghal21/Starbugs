from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="blood_donate"),
    path("submitted",views.submitblood,name="submitblood"),
    path("donate",views.donate,name="donate"),
    path("confirm",views.confirm,name="confirm")
]