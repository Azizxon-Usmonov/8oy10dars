
from django.urls import path
from .views import Teacher, Student

urlpatterns = [
    path('register/teacher/', Teacher.as_view(), name='register-teacher'),
    path('register/student/', Student.as_view(), name='register-student'),
]
