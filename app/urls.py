from django.contrib import admin
from django.urls import path
from .views import *
from django.urls import path


urlpatterns = [
    path('create_dept/',add_department.as_view(),name='create_dept'),
    path('views_dept/<int:id>',add_department.as_view(),name='add_department'),
    path('all_views_dept/',All_dataget.as_view(),name='add_department'),
    path('update_dept/<int:id>',add_department.as_view(),name='add_department'),
    path('delete_dept/<int:id>',DeleteAccountView.as_view(),name='delete'),
    
    path('create_desg/',Add_Designation.as_view(),name='create_desg'),
    path('views_desg/<int:id>',Add_Designation.as_view(),name='views_desg'),
    path('all_views_desg/',Alldataget.as_view(),name='views_desg'),
    path('update_desg/<int:id>',Add_Designation.as_view(),name='update_desg'),
    path('delete_desg/<int:id>',Add_Designation.as_view(),name='delete_desg'),
    
    
    
    
    
    
    
    
        
]
