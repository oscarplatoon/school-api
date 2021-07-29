from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    credits = models.IntegerField()


class Student(models.Model):
    student_name = models.CharField(max_length=255)
    courses = models.ManyToManyField(related_name='students')