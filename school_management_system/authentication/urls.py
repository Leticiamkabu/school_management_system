from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/',RegisterationView.as_view(), name = 'Register'),
    path('student/registeration/', StudentRegisterationView.as_view(), name='student_registeration'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('teacher/registeration/', TeacherRegisterationView.as_view(), name='teacher_registeration'),
]