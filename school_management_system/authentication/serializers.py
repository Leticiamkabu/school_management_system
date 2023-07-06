from rest_framework import serializers
from .models import *

class UserDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SystemUserData
        fields = ['first_name','last_name','username', 'email', 'password','status']
        
    def create(self, validated_data):
        user = SystemUserData.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            status = validated_data['status']
        )
        
        user.set_password(validated_data['password'])
        user.save()
        
        return user

class StudentRegisterationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudentRegisteration
        fields = ['username','password', 'level', 'admission_number']
        
        
    def create(self, validated_data):
        student = StudentRegisteration.objects.create(
            username = validated_data['username'],
            level = validated_data['level'],
            admission_number = validated_data['admission_number'],
            password = validated_data['password']
        )
        
        # student.set_password(validated_data['password'])
        student.save()
        return student
    
class TeacherRegisterationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TeacherRegisteration
        fields = ['username', 'password', 'position','application_number']
        
        def create(self, validated_data):
            
            teacher = TeacherRegisteration.objects.create(
                username = validate_data['username'],
                password = validated_data['passowrd'],
                position = validated_data['position'],
                application_number = validated_data['application_number'],
            )
            
            teacher.save()
            return teacher