from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from dashboard.views import *

router = routers.DefaultRouter()
router.register(r'faculties', FacultyModelViewSet)
router.register(r'departments', DepartmentModelViewSet)
router.register(r'groups', GroupModelViewSet)
router.register(r'subjects', SubjectModelViewSet)
router.register(r'teacher', TeacherModelViewSet)
router.register(r'student', StudentModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
