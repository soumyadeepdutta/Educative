# from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Course


class HomeView(ListView):
    model = Course
    template_name = 'base/home.html'


class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
