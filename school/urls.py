from django.urls import path
from . import views

urlpatterns = [
    #Student paths:
    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('students/new', views.new_student, name='new_student'),
    path('students/<int:student_id>/edit/', views.edit_student, name='edit_student'),
    path('students/<int:student_id>/delete/', views.delete_student, name='delete_student'),
    #Course paths:
    path('courses/', views.course_list, name='course_list'),
    #returns both course details and all enrolled students
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('courses/new', views.new_course, name='new_course'),
    path('courses/<int:course_id>/edit/', views.edit_course, name='edit_course'),
    path('courses/<int:course_id>/delete/', views.delete_course, name='delete_course'),
]
