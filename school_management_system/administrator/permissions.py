from rest_framework import permissions

class Admin_priviledge(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        return False

    
class Student_priviledge(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.status == Student:
            return True

        return False


class Teacher_priviledge(permissions.BasePermission):
    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.status == Teacher:
            return True

        return False