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
    path('about/', views.AboutView.as_view(), name='about'),
    path('test/', views.TestView.as_view(), name='test'),
    path('umi-random/', views.UmiRandomView.as_view(), name='umi-random'),
    path('amp-bias/', views.AmpBiasView.as_view(), name='amp-bias'),
    path('gene-bias/', views.GeneBiasView.as_view(), name='gene-bias'),
    path('mammal-data/', views.MammalDataView.as_view(), name='mammal-data'),
]
