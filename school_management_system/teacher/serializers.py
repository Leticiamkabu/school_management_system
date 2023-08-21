from rest_framework import serializers
from administrator.models import Course

class Get_Course_Detail_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ['name', 'description', 'course_number', 'level', 'teacher', 'student', 'registered_students']