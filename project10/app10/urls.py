from django.urls import path
from .views import BankDetail,bankinfo,AddressDetail,addressinfo
urlpatterns=[

    path('bank/',BankDetail.as_view()),
    path('bank/<int:id>/',bankinfo.as_view()),
    path('address/',AddressDetail.as_view()),
    path('address/<int:id>/',addressinfo.as_view()),
    # path('merged/', MergedAPIView.as_view(), name='merged-api'),
]