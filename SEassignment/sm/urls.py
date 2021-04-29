# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:41:32 2020

@author: dell
"""

from django.urls import path
from . import views

app_name = 'sm'
urlpatterns=[
    ###### PRIMARY MENU #######
    path('', views.List.as_view(), name='menu'),
    
    ###### DETAIL PAGES URL SETTINGS #######
    path('<int:pk>/cashier', views.Cashier.as_view(), name='cashier'),
    path('<int:pk>/inventoryincrement/', views.Inventoryincrement.as_view(), name='inventoryincrement'),
    path('<int:pk>/inventorydecrement/', views.Inventorydecrement.as_view(), name='inventorydecrement'),
    path('<int:pk>/inventory/', views.Inventory.as_view(), name='inventory'),
    path('<int:pk>/monthly/', views.Monthly.as_view(), name='monthly'),
    path('<int:pk>/yearly/', views.Yearly.as_view(), name='yearly'),
    
    ###### SECONDARY MENU && DETAIL PAGES URL SETTINGS #######
    path('<int:pk>/retail/', views.Retail.as_view(), name='retail'),
    
    ###### RESULTS PAGES URL SETTINGS #######
    path('<int:pk>/cashresults/',views.CashResults.as_view(),name='cashresults'),
    path('<int:pk>/inresults/',views.InResults.as_view(),name='inresults'),
    path('<int:pk>/deresults/',views.DeResults.as_view(),name='deresults'),
    path('<int:pk>/stockresults/',views.StockResults.as_view(),name='stockresults'),
    path('<int:pk>/monthlyresults/',views.MonthlyResults.as_view(),name='monthlyresults'),
    path('<int:pk>/yearlyresults/',views.YearlyResults.as_view(),name='yearlyresults'),

    ###### PROCESSOR URL SETTINGS #######
    path('<int:pk>/cash/',views.cash,name='cash'),
    path('<int:pk>/increase/',views.increase,name='increase'),
    path('<int:pk>/decrease/',views.decrease,name='decrease'),
    path('<int:pk>/stock/',views.stock,name='stock'),
    path('<int:pk>/month/',views.month,name='month'),
    path('<int:pk>/year/',views.year,name='year'),

        ]












