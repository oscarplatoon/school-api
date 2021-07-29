from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import StudentForm, CourseForm
from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer
import json

def get_student(student_id):
    return Student.objects.get(id=student_id)


def get_course(course_id):
    return Course.objects.get(id=course_id)


def student_list(request):
    students = Student.objects.all()
    serialized_students=StudentSerializer(students).all_students
    return JsonResponse(serialized_students, status=200)


def student_detail(request, student_id):
    student= get_student(student_id)
    serialized_student=StudentSerializer(student).student_detail
    return JsonResponse(serialized_student, status=200)


@csrf_exempt
def new_student(request):
    if request.method == 'POST':
        data = json.load(request)
        form = StudentForm(data)
        if form.is_valid():
            student = form.save(commit=True)
            serialized_student=StudentSerializer(student).student_detail
            return(JsonResponse(data=serialized_student, status=200))


@csrf_exempt
def edit_student(request, student_id):
    student = get_student(student_id)
    if request.method == 'POST':
        data = json.load(request)
        form = StudentForm(data, instance=student)
        if form.is_valid():
            student = form.save(commit=True)
            serialized_student=StudentSerializer(student).student_detail
            return(JsonResponse(data=serialized_student, status=200))


@csrf_exempt
def delete_student(request, student_id):
    if request.method == "POST":
        student=get_student(student_id)
        student.delete()
        return(JsonResponse(data={'status':'Successfully Deleted Student'}, status=200))

###
def course_list(request):
    courses = Course.objects.all()
    serialized_courses=CourseSerializer(courses).all_courses
    return JsonResponse(serialized_courses, status=200)


def course_detail(request, course_id):
    course= get_course(course_id)
    serialized_course=CourseSerializer(course).course_detail
    return JsonResponse(data=serialized_course, status=200)


@csrf_exempt
def new_course(request):
    if request.method == 'POST':
        data = json.load(request)
        form = courseForm(data)
        if form.is_valid():
            course = form.save(commit=True)
            serialized_course=CourseSerializer(course).course_detail
            return(JsonResponse(data=serialized_course, status=200))


@csrf_exempt
def edit_course(request, course_id):
    course = get_course(course_id)
    if request.method == 'POST':
        data = json.load(request)
        form = courseForm(data, instance=course)
        if form.is_valid():
            course = form.save(commit=True)
            serialized_course=CourseSerializer(course).course_detail
            return(JsonResponse(data=serialized_course, status=200))


@csrf_exempt
def delete_course(request, course_id):
    if request.method == "POST":
        course=get_course(course_id)
        course.delete()
    return(JsonResponse(data={'status':'Successfully Deleted course'}, status=200))

@csrf_exempt
def add_student(request, course_id, student_id):
    if request.method == "POST":
        student = get_student(student_id)
        course_to_add = get_course(course_id)
        student.courses.add(course_to_add)
    return(JsonResponse(data={'status':'Successfully added student to course'}, status=200))


@csrf_exempt
def remove_student(request, course_id, student_id):
    if request.method == "POST":
        student = get_student(student_id)
        course_to_remove = get_course(course_id)
        student.courses.remove(course_to_remove)
    return(JsonResponse(data={'status':'Successfully removed student from the course'}, status=200))