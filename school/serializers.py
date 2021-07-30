from rest_framework import serializers
from .models import Student, Course

# depth = 1 for the models
# Includes the serialized output of the courses to which the student is enrolled
# (makes the json object contain *all* the data)

class StudentSerializer(serializers.ModelSerializer):
    # If you only want limited data passed, you can use this to pass the title
    # __str__ method for the related model.
    # courses = serializers.StringRelatedField(many=True)
    class Meta:
        model = Student
        fields = ['id', 'student_name', 'courses']
        depth = 1


class CourseSerializer(serializers.ModelSerializer):
    # students = serializers.StringRelatedField(many=True)
    class Meta:
        model = Course
        fields = ['id', 'title', 'credits', 'students']
        depth = 1