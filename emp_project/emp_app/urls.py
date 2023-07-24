
from django.urls import path
from .views import *
urlpatterns = [

    path('emp/',personal_detail_view.as_view()),
    path('emp/<int:id>/',Employeeinfo.as_view()),

    path('document/',document_detail.as_view()),
    path('document/<int:id>/',Document_info.as_view()),

    path('emergency/',emergencycontact_view.as_view()),
    path('emergency/<int:id>/',emergencycontact_info.as_view()),

    path('salary/',salary_view.as_view()),
    path('salary/<int:id>/',salary_info.as_view()),

    path('socialmeadia/',socialmeadia_view.as_view()),
    path('socialmeadia/<int:id>/',socialmeadia_info.as_view())
]
