from django import views
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', views.were, name='werey'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.home, name='home'),
    path('c_list/', views.c_list, name='c_list'),
    path('c_info/<int:pk>/', views.c_info, name='c_info'),
    path('cstock/<int:pk>/', views.cstock, name='cstock'),
    path('cstock/<int:pk>/cstock_reg/', views.cstock_reg, name='cstock_reg'),
    path('addc/', views.addc, name='addc'),
]