from rest_framework import serializers
from administrator.models import Course
from authentication.serializers import TeacherRegisterationSerializer


class GetCourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ['name', 'description','course_number', 'level', 'teacher']
        
        
class RegisterCourseSerializer(serializers.ModelSerializer):
    teacher = TeacherRegisterationSerializer()
    class Meta:
        model = Course
        fields = ['name', 'description', 'course_number', 'level','teacher', 'student','registered_students']