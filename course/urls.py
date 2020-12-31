from django.urls import path
from . import views


app_name = 'course'
urlpatterns = [
    path('access/<int:pk>', views.AccessCourse.as_view(), name='access'),
    path('enroll/<int:pk>', views.enroll, name='enroll'),
    path('courses/<int:pk>', views.CourseDetailView.as_view(), name="courseDetail"),
    path('courses', views.CourseListView.as_view(), name="courseList"),
    path('', views.HomeView.as_view(), name="home"),
]
