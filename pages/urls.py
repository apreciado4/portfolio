# pages/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from pages import views
from portfolio import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('success/', views.success, name='success'),
    path('projects/', include('projects.urls')),

]