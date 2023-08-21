from django.urls import path
from .views import *

urlpatterns = [
    path('course/<int:teacher_id>/', Get_course_detail.as_view(), name = 'get_course_details')
]
