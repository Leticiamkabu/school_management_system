from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from administrator.models import *
from .permissions import *

# Create your views here.

# urlpatterns = [
#     path('admission_form/', Admission_view.as_view(), name = 'admission-form'),
#     path('application_form/', Application_view.as_view(), name = 'application-form'),
#     path('payment_form/<str:name
# >/', PaymentView.as_view(), name = 'payment_update'),
#     path('course/', CourseView.as_view(), name = 'courses'),
    
# ]


class Admission_view(APIView):

    def post(self, request):

        serializer = Admission_Forms_detailSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data)


    def get(self, request):
        # create permission file
        queryset = Admission_Forms_detail.objects.all()
        serializer = Admission_Forms_detailSerializer(queryset, many=True)

        for applicant in queryset:
            if applicant.status == 'Pending Approval' and int(applicant.grade) <= 15:
                applicant.status = 'Approved'
                applicant.save()


        return Response(serializer.data)
            
        
    

class Application_view(APIView):

    def post(self, request):

        serializer = Application_form_detailSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data)


    def get(self, request):
        # create permission file
        permission_classes = (Admin_priviledge)
        queryset = Application_Form_detail.objects.all()
        serializer = Application_form_detailSerializer(queryset, many=True)

        for applicant in queryset:
            if applicant.duration_of_work == 'Full time':
                applicant.status = 'Approved'
                applicant.save()


        return Response(serializer.data)

    
    

class PaymentView(APIView):

    def get(self, request, name):
        permission_classes = (Student_priviledge, Admin_priviledge)
        queryset = Student_Payment_Details.objects.filter(name = name)
        serializer = Student_Payment_DetailsSerializer(queryset, many = True)

        
        return Response(serializer.data)
    
    def patch(self, request, name):
        permission_classes = (Admin_priviledge)
        queryset = Student_Payment_Details.objects.get(name = name)
        serializer = Student_Payment_DetailsSerializer(instance = queryset, data = request.data, partial=True)
        
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)
    
   
   

class CourseView(APIView):

    def post(self, request):

        permission_classes = (Admin_priviledge)
        serializer = CourseSerializer(data = request.data)
        serializers.is_valid(raise_exception = True)
        serializer.save()

        return Response(serilizer.data)
    

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
                
            


