"""adminStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from inventory.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name = 'index'),
     #Manage Distributor
    path('createDistributor/', createDistributor, name = 'create_Distributor'),
    path('showDistributor/', showDistributor, name = 'show_Distributor'),
    path('editDistributor/<int:id>/', editDistributor, name = 'edit_Distributor'),
    path('deletDistributor/<int:id>/', deleteDistributor, name = 'delete_Distributor'),
    #Manage Item
    path('createItem/', createItem, name = 'create_Item'),
    path('showItem/', showItem, name = 'show_Item'),
    path('editItem/<int:id>/', editItem, name = 'edit_Item'),
    path('deletItem/<int:id>/', deleteItem, name = 'delete_Item'),
    #Manage User
    path('createUser/', createUser, name = 'create_User'),
    path('showUser/', showUser, name = 'show_User'),
    path('editUser/<int:id>/', editUser, name = 'edit_User'),
    path('deletUser/<int:id>/', deleteUser, name = 'delete_User'),
    #Manage Invoice
    path('createInvoice/', createInvoice, name = 'create_Invoice'),
    path('showInvoice/', showInvoice, name = 'show_Invoice'),
    path('editInvoice/<int:id>/', editInvoice, name = 'edit_Invoice'),
    path('deletInvoice/<int:id>/', deleteInvoice, name = 'delete_Invoice'),
    #Manage Point
    path('createPoint/', createPoint, name = 'create_Point'),
    path('showPoint/', showPoint, name = 'show_Point'),
    path('editPoint/<int:id>/', editPoint, name = 'edit_Point'),
    path('deletPoint/<int:id>/', deletePoint, name = 'delete_Point'),
    #Manage Detail
    path('createDetail/', createDetail, name = 'create_Detail'),
    path('showDetail/', showDetail, name = 'show_Detail'),
    path('editDetail/<int:id>/', editDetail, name = 'edit_Detail'),
    path('deletDetail/<int:id>/', deleteDetail, name = 'delete_Detail'),
    
    

]
