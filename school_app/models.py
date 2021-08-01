from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    credits = models.IntegerField()

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    courses = models.ManyToManyField(Course, name="students", blank=True)
    
    def __str__(self):
        return self.name
