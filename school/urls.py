from django.urls import path, include
from rest_framework import urlpatterns
from .views import StudentViewSet, CourseViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns= router.urls
