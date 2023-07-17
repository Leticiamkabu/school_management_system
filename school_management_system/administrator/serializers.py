from rest_framework import serializers
from .models import *


class Admission_Forms_detailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Admission_Forms_detail
        fields =['form_id','date','admission_number','image', 'first_name','last_name', 'age', 'email', 'phone_number','level', 'grade', 'date_of_birth', 
                 'place_of_birth', 'nationality','gender', 'residential_address', 
                 'language', 'mother_name', 'father_name' , 'status']
     
        
    def create(self, validated_data):
        student = Admission_Forms_detail.objects.create(
            
            image = validated_data['image'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            age = validated_data['age'],
            email = validated_data['email'],
            phone_number = validated_data['phone_number'],
            level = validated_data['level'],
            grade = validated_data['grade'],
            date_of_birth = validated_data['date_of_birth'],
            place_of_birth = validated_data['place_of_birth'],
            nationality = validated_data['nationality'],
            gender = validated_data['gender'],
            residential_address = validated_data['residential_address'],
            language = validated_data['language'],
            mother_name = validated_data['mother_name'],
            father_name = validated_data['father_name']
        )
        
        student.save()
        
        return student
    
    
class Application_form_detailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Application_Form_detail
        fields = ['first_name','last_name', 'contact', 'email', 'location', 'application_position', 'certificate', 'work_experience', 'reference', 'duration_of_work', 'status']
        
    def create(self,validated_data):
        teacher = Application_Form_detail.objects.create(
            first_name= validated_data['first_name'],
            last_name = validated_data['last_name'],
            contact = validated_data['contact'],
            email = validated_data['email'],
            location = validated_data['location'],
            application_position = validated_data['application_position'],
            certificate = validated_data['certificate'],
            work_experience = validated_data['work_experience'],
            reference = validated_data['reference'],
            duration_of_work = validated_data['duration_of_work']
        )
        
        teacher.save()
        
        return teacher
    
class Student_Payment_DetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student_Payment_Details
        fields = ['student','level','total_amount','name','amount_paid', 'amount_left' ]
        
    
    
    
    
class CourseSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Course
        fields = ['name', 'description', 'level',]
        
    def create(self, validated_data):
        
        course = Course.objects.create(
            name = validated_data['name'],
            description = validated_data['description'],
            level = validated_data['level']
            
        )
        
        course.save()
        
        return course
    
    