from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name = 'index'),
    path('profile/', views.user_profile, name='profile'),
    path('accounts/profile/', views.index,name='profile'),
    path('create_profile/',views.create_profile,name = 'create_profile'),


]