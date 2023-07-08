from django.urls import path
from .views import *


urlpatterns = [
    path('course_detail/<str:level>/', Course_details.as_view(), name = 'course detail')
]
