from django.urls import path
from . import views


urlpatterns= [
    path("",views.index,name="leave"),
    path("ViewApplications/",views.viewApplications,name="ViewApplications"),
    path("Application_Response/", views.Application_response,name="Application_Response")
]