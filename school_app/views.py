## wines/views.py
from .models import Student
from .models import Course
from .serializers import StudentSerializer
from .serializers import CourseSerializer
from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

