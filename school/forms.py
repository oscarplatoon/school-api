from django import forms
from .models import Student, Course


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('student_name', 'courses')


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'credits')