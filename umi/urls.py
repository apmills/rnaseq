"""
App URLs
"""
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'umi'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('test/', views.TestView.as_view(), name='test'),
    path('umi-random/', views.UmiRandomView.as_view(), name='umi-random'),
]
