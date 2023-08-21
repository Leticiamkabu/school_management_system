from django.shortcuts import render
from administrator.models import Course
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from administrator.permissions import *
from authentication.models import TeacherRegisteration

# Create your views here.

class Get_course_detail(APIView):
    
    # queryset = Course.objects.all()
    
    def get(self,request, teacher_id):
        for teachers in TeacherRegisteration.objects.all():
            if teachers.teacher_id == teacher_id:
                teacher = teachers.id
        permission_classes = (Teacher_priviledge,)
        queryset = Course.objects.filter(teacher = teacher)
        serializer = Get_Course_Detail_Serializer(queryset, many = True)
        return Response(serializer.data)
        
        
