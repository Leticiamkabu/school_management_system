from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from administrator.models import Course
from .serializer import *
from administrator.permissions import *
from authentication.models import StudentRegisteration, SystemUserData
import jwt
from django.conf import settings


# Create your views here.

#get all course details acording to student level
class Course_details(APIView):
    
    def get(self, request, level, format= None):
        permission_classes = (Student_priviledge)
        queryset = Course.objects.filter(level = level)
        
        serializer = GetCourseSerializer(queryset, many = True)
        
        return Response(serializer.data)
    
    
class Course_registeration(APIView):
    # patching a many to many field and making sure the user is authorized for theis action.
    def patch(self,request, registered_student_id):
        student = StudentRegisteration.objects.get(registered_student_id = registered_student_id)
        # permission_classes = (Student_privilege,)
        queryset = Course.objects.filter(level = student.level)
        token = request.headers.get('Authorization', None)
        modified_token = token.replace('Bearer ','')
        
        
        if modified_token:
            decoded_token = jwt.decode(modified_token, settings.SECRET_KEY, algorithms = ['HS256'])
            
            for users in SystemUserData.objects.all():
                if users.username == student.username:
                    
                    if users.id in decoded_token.values():
                      
                        for courses in queryset:
            
                            if courses.level == student.level:
                               
                                if courses.registered_students == 'None' or  courses.registered_students == []:
                                    student = StudentRegisteration.objects.get(registered_student_id = registered_student_id)
                                    courses.registered_students.add(student)
                        
                                if courses.registered_students != 'None':
                                    student = StudentRegisteration.objects.get(registered_student_id = registered_student_id)
                                    courses.registered_students.add(student)
                            else:
                                pass
                        
                    else:
                        # print("No")
                        # print(users.id)
                        return Response({'Your are not required to access this functionality':'Thank you'})    
                
       
        serializer = RegisterCourseSerializer(queryset, many = True)
        
        
        return Response(serializer.data)
        

