from django.urls import path
from .views import *


urlpatterns = [
    path('course_detail/<str:level>/', Course_details.as_view(), name = 'course detail'),
    path('course_registeration/<int:registered_student_id>/', Course_registeration.as_view(), name = 'course registeration')
]
# Course_registeration