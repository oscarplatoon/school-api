from .views import StudentViewSet
from .views import CourseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'courses', CourseViewSet, basename='course')
urlpatterns = router.urls
