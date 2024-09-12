from rest_framework import serializers
from .models import *


class FacultyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class DepartmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class GroupModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class SubjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class TeacherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

