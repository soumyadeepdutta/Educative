from django.urls import path
from . import views


app_name = 'course'
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('courses', views.CourseListView.as_view(), name="courseList"),
    path('courses/<int:pk>', views.CourseDetailView.as_view(), name="courseDetail")
]
