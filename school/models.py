from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    credits = models.IntegerField()

    def __str__(self) -> str:
        return f"COURSE NAME: {self.title}"


class Student(models.Model):
    student_name = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course, related_name='students', blank=True)

    def __str__(self) -> str:
        return f"STUDENT NAME: {self.student_name}"