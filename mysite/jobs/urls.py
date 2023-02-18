from django.urls import path
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('seccess/<str:activation_key>/', views.success, name='success'),
    path('apply_job/<str:job_title>/', views.apply_job, name='apply_job'),
    path('activate/<str:activation_key>/',
         views.activate_job_application, name='activate_job_application'),
]
