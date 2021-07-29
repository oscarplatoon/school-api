from django.urls import path
from . import views

urlpatterns = [
    #Student paths:
# - Read all the students in the school 
    path('students/', views.student_list, name='student_list'),
# - Read data for one particular student 
# - See all of a student's current Courses 
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
# - Create new students 
    path('students/new', views.new_student, name='new_student'),
# - Update student records
    path('students/<int:student_id>/edit/', views.edit_student, name='edit_student'),
# - Delete a student
    path('students/<int:student_id>/delete/', views.delete_student, name='delete_student'),
    #Course paths:
    path('courses/', views.course_list, name='course_list'),
# - Create, 
    path('courses/new', views.new_course, name='new_course'),
# Read, 
    #returns both course details and all enrolled students
# - See all the students currently enrolled in a course 
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
# Update, 
    path('courses/<int:course_id>/edit/', views.edit_course, name='edit_course'),
# and Destroy a course 
    path('courses/<int:course_id>/delete/', views.delete_course, name='delete_course'),
# - Enroll a student in a course
    path('courses/<int:course_id>/add/<int:student_id>/', views.add_student, name='add_student'),
# - Remove a student from a course
    path('courses/<int:course_id>/remove/<int:student_id>/', views.remove_student, name='add_student'),
]
