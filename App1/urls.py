from django.urls import path
from .views import *
urlpatterns = [
    path('work_shift/', WorkShifCreateView.as_view(), name='work_shift_create'),
    path('work_shift/<int:id>/', WorkShifCreateView.as_view(), name='get_data'),
    path('data_workShift/',Alldataget.as_view(),name='All_data_workShift')
    
]