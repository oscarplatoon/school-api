from django import forms
from django.db.models import fields
from school_app.models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name')

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'description')