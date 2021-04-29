# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:19:36 2019

@author: dell
"""

from django.urls import path
from . import views

app_name= 'loan'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('<int:pk>/results/',views.ResultsView.as_view(),name='results'),
    path('<int:pk>/info/',views.info,name='info'),

]