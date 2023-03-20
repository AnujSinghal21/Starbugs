from django.urls import path
from . import views

urlpatterns = [
    path('add_health_record',views.add_health_record,name = 'add_health_records'),
    path('create_health_record', views.create_health_record, name='create_health_record'),
    path('health_records', views.view_health_records, name='health_records'),
    path('home_health_record',views.home_health_record,name = 'home_health_record')
    # path('',views.option_check,name = 'option_check')
]