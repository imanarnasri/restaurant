from . import views
from django.urls import path

urlpatterns = [

    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('reservations', views.New_reservation_view.as_view(), name='reservations'),
    path('contact', views.contact, name='contact'),
    #registration endpoint
    path('login',views.login_view,name='login'),
    #login endpoint
    path('register',views.register,name='register'),
    #logout endpoint
    path('logout',views.logout_view, name = 'logout'),

    path('chatbot', views.chatbot, name='chatbot'),

    path('listmenu/<str:cat>',views.list_menu.as_view(),name = 'list_menu'),
    path('thanks',views.thank,name = 'thank')

]
