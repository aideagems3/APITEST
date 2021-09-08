"""api_picfortrain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from uploadpic import views

urlpatterns = [
    # path('testjson/', views.testjson,name='testjson'),
    # path('testjsondetail/<int:pk>', views.testjson_detail,name='testjson_detail'),
    path('reqresjson/', views.reqresjson,name='reqresjson'),
    path('mypostapi/', views.mypostapi,name='mypostapi'),
    path('voltage-list/', views.VoltageList.as_view(),name='voltage-list'),
    path('voltage-detail/<int:pk>', views.VoltageDetial.as_view(),name='voltage-detail'),
    path('equipment-list/', views.EquipmentList.as_view(),name='equipment-list'),
    path('equipment-detail/<int:pk>', views.EquipmentDetial.as_view(),name='equipment-detail'),
    path('sub_equipment-list/', views.Sub_equipmentList.as_view(),name='sub_equipment-list'),
    path('sub_equipment-detail/<int:pk>', views.Sub_equipmentDetial.as_view(),name='sub_equipment-detail'),
    path('abnormal-list/', views.AbnormalList.as_view(),name='abnormal-list'),
    path('abnormal-detail/<int:pk>', views.AbnormalDetial.as_view(),name='abnormal-detail'),
    path('job_upload-list/', views.Job_uploadList.as_view(),name='job_upload-list'),
    path('job_upload-detail/<int:pk>', views.Job_uploadDetial.as_view(),name='job_upload-detail'),
  
    
    

]
