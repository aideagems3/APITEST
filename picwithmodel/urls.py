
from django.contrib import admin
from django.urls import path
from picwithmodel import views

urlpatterns = [
    path('imageformodelList/', views.ImageformodelList.as_view(),name='ImageformodelList'),

]
