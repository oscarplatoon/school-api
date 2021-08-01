from rest_framework import serializers
from .models import Student
from .models import Course

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'age', 'courses']
        depth = 1

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'description', 'credits']
        depth = 1
        
