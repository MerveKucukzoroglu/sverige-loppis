""" Loppis App urls file """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_loppis, name='loppis'),
]
