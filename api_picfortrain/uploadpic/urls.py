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
    # path('admin/', admin.site.urls),
    # path('test_json/', views.test_json,name='test_json'),
    path('voltage/', views.voltage),
    path('equipment/', views.EquipmentGenericsView.as_view()),
    path('sub_equipment/', views.Sub_equipmentGenericsView.as_view()),
    path('abnormal/', views.AbnormalGenericsView.as_view()),
    path('job_upload/', views.Job_uploadGenericsView.as_view()),
    path('testjson/', views.testjson,name='testjson'),
    path('reqresjson/', views.reqresjson,name='reqresjson'),
    path('mypostapi/', views.mypostapi,name='mypostapi'),
    
    path('uploadSomething/', views.uploadSometing,name='uploadSometing'),
    path('readSomething/', views.readSomething,name='readSomething'),



]
