
from rest_framework import serializers
from .models import User, Teacher, Student

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'type')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = ('user', 'subject')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['type'] = 'teacher'
        user = UserSerializer().create(user_data)
        teacher = Teacher.objects.create(user=user, **validated_data)
        return teacher


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ('user', 'grade')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['type'] = 'student'
        user = UserSerializer().create(user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student
