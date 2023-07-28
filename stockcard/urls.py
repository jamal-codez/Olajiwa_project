from django import views
from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    #path('', views.were, name='werey'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),
    path('c_list/', views.c_list, name='c_list'),
    path('c_info/<int:pk>/', views.c_info, name='c_info'),
    path('cstock/<int:pk>/', views.cstock, name='cstock'),
    path('cstock/<int:pk>/cstock_reg/', views.cstock_reg, name='cstock_reg'),
    path('addc/', views.addc, name='addc'),
    path('delete_data/<int:pk>/<int:pc>/', views.del_rec, name='delete_data'),
    path('del_u/<int:pk>/', views.del_u, name='del_u')
]