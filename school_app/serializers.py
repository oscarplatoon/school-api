
from rest_framework import serializers
from school_app.models import Student, Course

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'description']




# class StudentSerializer(object):
#     def __init__(self, body):
#         self.body = body

#     @property
#     def all_students(self):
#         output = {'students': []}
#         for student in self.body:
#             student_details = {
#                 'first_name': student.first_name,
#                 'last_name': student.last_name,
#             }
#             output['students'].append(student_details)
#         return output

#     @property
#     def student_detail(self, student_id):
#         return {
#             'first_name': self.body.first_name,
#             'last_name': self.body.last_name,
#         }
