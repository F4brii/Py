from rest_framework import serializers
from schedule.models import Teacher, Student, Course, TeacherCourse, StudentCourse
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Teacher
        fields = ['id', 'user', 'code_institutional']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'maxLength', 'minLength', ]


class TeacherCourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer()
    course = CourseSerializer()

    class Meta:
        model = Course
        fields = ['teacher', 'course' ]


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Student
        fields = ['id', 'user', 'code_institutional']


class StudentCourseSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    course = serializers.StringRelatedField(many=True)

    class Meta:
        model = Course
        fields = ['student', 'course' ]