from django.shortcuts import render
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import *
from .models import *



# Create your views here.

class Admission_view(APIView):
    
    def post(self, request):
        serializer = Admission_Forms_detailSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        
        
        return Response(serializer.data)
    
    def get(self, request):
        
       
        queryset = Admission_Forms_detail.objects.all()
        permission_classes = (Admin_priviledge,)
        
        
        
        for admission_approval in queryset:
            if int(admission_approval.grade) <= 15:
                admission_approval.status = 'Approved'
            
            elif int(admission_approval.grade) > 15:
                admission_approval.status = 'Rejected'
                
            admission_approval.save()
        
    
           
        serializer = Admission_Forms_detailSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def delete(self,request):
        
        permission_classes = (Admin_priviledge)
        queryset = Application_Form_detail.objects.filter(status = 'Regected' )
        
        for appilcation_rejected in queryset:
            application_rejected.delete()
            
        return Response({"Applicant details deleted":" You have successfully deleted the applicants detail"})
    
    


class Application_view(APIView):
    
    def post(Self, request):
        serializer = Application_form_detailSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        
        return Response(serializer.data)
    
    def get(self, request):
        
        permission_class = (Admin_priviledge,)
        queryset = Application_Form_detail.objects.all()
        
        for application_approval in queryset:
            if application_approval.duration_of_work =='Full Time':
                application_approval.status = 'Approved'
            
            elif application_approval.duration_of_work =='Part Time':
                application_approval.status = 'Rejected'
                
            application_approval.save()
                
            
            
            
        serializer = Application_form_detailSerializer(queryset, many = True )
        
        return Response(serializer.data)
    
    def delete(self,request):
        
        permission_classes = (Admin_priviledge)
        queryset = Application_Form_detail.objects.filter(status = 'Rejected' )
        
        for application_rejected in queryset:
            application_rejected.delete()
            
        return Response({"Applicant details deleted":" You have successfully deleted the applicants detail"})
    
    
class PaymentView(APIView):
    
    def patch(self,request,name,format=None):
        permission_classes = (Admin_priviledge)
        queryset = Student_Payment_Details.objects.get(name = name)
    
    
        serializer = Student_Payment_DetailsSerializer(queryset, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
    
    
        
    def post(self, request):
        permission_classes = (Admin_priviledge)
        
        
        serializer = Student_Payment_DetailsSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        
        return Response(serializer.data)
        
    
class CourseView(APIView):
    
    def post(self, request):
        permision_classes = (Admin_priviledge)
        
        serializer = CourseSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        
        return Response(serializer.data)
    
    