from rest_framework import viewsets
from .serializers import *
from .models import *


class FacultyModelViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultyModelSerializer


class DepartmentModelViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentModelSerializer


class GroupModelViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer


class SubjectModelViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectModelSerializer


class TeacherModelViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherModelSerializer


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
