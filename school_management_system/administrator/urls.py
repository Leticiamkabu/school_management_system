from django.urls import path
from .views import *

urlpatterns = [
    path('admission_form/', Admission_view.as_view(), name = 'admission-form'),
    path('application_form/', Application_view.as_view(), name = 'application-form'),
    path('payment_form/<str:name>/', PaymentView.as_view(), name = 'payment_update'),
    path('course/', CourseView.as_view(), name = 'courses'),
    
]
