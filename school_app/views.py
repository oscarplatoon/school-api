from .models import *
from .serializers import *
from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = CourseSerializer





# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .forms import *
# from .models import Student
# from .serializers import StudentSerializer
# import json

# def student_list(request):
#     students = Student.objects.all()
#     serialized_students = StudentSerializer().all_students(students)
#     return JsonResponse(data=serialized_students, status=200)

# @csrf_exempt
# def student_new(request):
#     if request.method == "POST":
#         data = json.load(request)
#         form = StudentForm(data)
#         if form.is_valid():
#             student = form.save(commit=True)
#             serialized_student = StudentSerializer().student_detail(student)
#             return JsonResponse(data=serialized_student, status=200)

# def student_detail(request, student_id):
#     student = Student.objects.get(id=student_id)
#     serialized_student = StudentSerializer().student_detail(student)
#     return JsonResponse(data=serialized_student, status=200)

            
# @csrf_exempt
# def student_edit(request, student_id):
#     student = Student.objects.get(id=student_id)
#     if request.method == "POST":
#         data = json.load(request)
#         form = StudentForm(data, instance=student)
#         if form.is_valid():
#             student = form.save(commit=True)
#             serialized_student = StudentSerializer(student).student_detail
#             return JsonResponse(data=serialized_student, status=200)

# @csrf_exempt
# def student_delete(request, student_id):
#     if request.method == "POST":
#         student = Student.objects.get(id=student_id)
#         student.delete()
#     return JsonResponse(data={'status': 'Successfully deleted student.'}, status=200)