from school_app.models import Course, Student
from django.contrib import admin
from school_app import *
# Register your models here.
admin.site.register(Student)
admin.site.register(Course)