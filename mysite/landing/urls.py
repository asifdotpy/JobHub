# import required module, function and/or class
from django.urls import path
from . import views

# create url patterns
# landing app root directory sets to website root directory
urlpatterns = [
    path('', views.index, name='index'),
]
