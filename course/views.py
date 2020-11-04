# from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.list import ListView as LV
from .models import Course
from .models import Category


class HomeView(LV):
    model = Course
    template_name = 'base/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
