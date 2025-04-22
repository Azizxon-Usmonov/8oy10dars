from django.shortcuts import render

# Create your views here.

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

class Teacher(View):
    def get(self, request):
        return HttpResponse("Teacher registration page")

class Student(View):
    def get(self, request):
        return HttpResponse("Student registration page")
n