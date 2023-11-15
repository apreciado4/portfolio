# pages/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from pages import views
from portfolio import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('success/', views.success, name='success'),
    path('resume/', views.resume, name='resume'),
    path('404/', views.server_404, name='Error 404'),
    path('500/', views.server_500, name='Error 500')
]