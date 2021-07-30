from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return (f"first: {self.first_name}, last: {self.last_name}")

class Course(models.Model):
    name = models.TextField()
    description = models.TextField()
    students = models.ManyToManyField(Student, related_name="courses")

    def __str__(self):
        return (f"name: {self.name}")