from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from administrator.models import Course
from .serializer import *
from administrator.permissions import *

# Create your views here.

#get all course details acording to student level
class Course_details(APIView):
    
    def get(self, request, level, format= None):
        permission_classes = (Student_priviledge)
        queryset = Course.objects.filter(level = level)
        
        serializer = GetCourseSerializer(queryset, many = True)
        
        return Response(serializer.data)

