from . import views 
from django.urls import path

urlpatterns = [
    path('appetizers', views.appetizers, name='appetizers'),
    path('beverages', views.beverages, name='beverages'),
    path('desserts', views.desserts, name='desserts'),
    path('maincourse', views.maincourse, name='maincourse'),

]
