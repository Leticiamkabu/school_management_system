from rest_framework import permissions
import jwt
# from authentication.models import Student_registeration


class Admin_priviledge(permissions.BasePermission):
    
    edit_methods = ("PUT", "PATCH")
    
    def has_object_permission(self, request,view, obj):
        
        if request.user.is_superuser:
            return True
   
# class Student_priviledge(permissions.BasePermission):
    
#     def has_object_permission(self, request,view, obj):
        
#         if request.user.status == 'Student':
#             return True
    
# class Student_privilege(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.user.is_authenticated and request.user.status == 'Student':
#             # Check if the user's token matches the token used for authentication
#             token = request.auth
#             if token and str(token) == str(request.user.auth_token):
#                 return True
#         return False
    
    
# class Student_privilege(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.user.is_authenticated and request.user.status == 'Student':
#             # Check if the user's token matches the token used for authentication
#             user_token = request.user.auth_token.key
#             request_token = request.META.get('HTTP_AUTHORIZATION').split()[1]
#             if user_token == request_token:
#                 return True
#         return False

# class Student_privilege(permissions.BasePermission):
#     def has_permission(self, request, view):
#         token = request.data.get('bearer ', None)
#         registration_id = request.data.get('registerd_student_id', None)
        
#         if token and registeration_id:
#             student = Student.objects.filter(token=token, registerd_student_id = registration_id).first()
#             if student and student.user == request.user:
#                 return True
#         return False
    
    
    
# class AuthorAllStaffAllButEditOrReadOnly(permissions.BasePermission):

    # edit_methods = ("PUT", "PATCH")

    # def has_permission(self, request, view):
    #     if request.user.is_authenticated:
    #         return True

    # def has_object_permission(self, request, view, obj):
    #     if request.user.is_superuser:
    #         return True

    #     if request.method in permissions.SAFE_METHODS:
    #         return True

    #     if obj.author == request.user:
    #         return True

    #     if request.user.is_staff and request.method not in self.edit_methods:
    #         return True

    #     return False



class Student_privilege(permissions.BasePermission):
    def has_permission(self, request, view):
        token = request.data.get('token', None)
        registration_id = request.data.get('registered_student_id', None)  # Corrected spelling of 'registered'

        if token and registration_id:
            try:
                decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                user_id = decoded_token.get('user_id')
                if user_id and str(user_id) == str(request.user.id):
                    student = SystemUserData.objects.filter(token=token,  user=request.user).first()
                    if student:
                        return True
            except jwt.exceptions.DecodeError:
                pass

        return False