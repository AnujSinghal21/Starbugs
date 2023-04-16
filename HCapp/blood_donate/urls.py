from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="blood_donate"),
    path("submitted",views.submitblood,name="submitblood"),
    path("closeRequest",views.closeRequest,name="closeRequest"),
    path("donate",views.donate,name="donate"),
    path("confirm",views.confirm,name="confirm")
]