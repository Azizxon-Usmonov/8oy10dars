from django.http import HttpResponse
from django.views import View

from school_project.permissions import IsAdmin, IsTeacher, IsStudent


class Teacher(View):
    permission_classes = [IsAdmin | IsTeacher]

    def get(self, request):
        if not any(perm().has_permission(request, self) for perm in self.permission_classes):
            return HttpResponse("Permission Denied", status=403)
        return HttpResponse("Teacher registration page")


class Student(View):
    permission_classes = [IsAdmin | IsStudent]  

    def get(self, request):
        if not any(perm().has_permission(request, self) for perm in self.permission_classes):
            return HttpResponse("Permission Denied", status=403)
        return HttpResponse("Student registration page")