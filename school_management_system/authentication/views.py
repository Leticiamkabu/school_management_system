from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from administrator.models import *

# Create your views here.

class RegisterationView(APIView):
    
    def post(self, request):
        serializer = UserDataSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        
        return Response(serializer.data)
    
    
class StudentRegisterationView(APIView):
    # check this functionaltity
    def post(self, request):
        
        student = 0
        for students in Admission_Forms_detail.objects.all():
            
            if students.admission_number == int(request.data.get('admission_number')) and students.status == 'Approved':
                student = int(request.data.get('admission_number'))
                
        if student == int(request.data.get('admission_number')):
            pass
        else:
            print(type(student))
            print(student)
            print(int(request.data.get('admission_number')))
            print(type(int(request.data.get('admission_number'))))  
            
            return Response({'Your admission was not approved':'Contact the school authorities or apply next time. Thank you'})
        
        serializer = StudentRegisterationSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()    
        
                
        return Response(serializer.data)
            

class TeacherRegisterationView(APIView):
    
    def post(Self, request):
    
        teacher = 0
        for teachers in Application_Form_detail.objects.all():
            
            if teachers.application_number == int(request.data.get('application_number')) and teachers.status == 'Approved':
                teacher = int(request.data.get('application_number'))
                
        if teacher == int(request.data.get('application_number')):
            pass
        else:
                
            return Response({'Your application was not approved':'Contact the school authorities or apply next time. Thank you'})
            
            
            
        serializer = TeacherRegisterationSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        
        
        return Response(serializer.data)
                
            