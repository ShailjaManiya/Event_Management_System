from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('services',views.services,name='serivces'),
    path('registration',views.registration,name='registration'),
    path('registration_new',views.registration_new,name='registration_new'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('Admin_login',views.Admin_login,name='Admin_login'),
    path('AdminPage',views.AdminPage,name='AdminPage'),
    path('After_login',views.After_login,name='After_login')
]