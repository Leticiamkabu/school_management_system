from rest_framework import serializers
from administrator.models import Course


class GetCourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ['name', 'description','course_number', 'level', 'teacher']
        