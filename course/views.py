from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Course, Enrollment
from .models import Category


class HomeView(ListView):
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


def enroll(request, pk):
    course = Course.objects.get(pk=pk)
    e, created = Enrollment.objects.get_or_create(student=request.user, course=course)
    return render(request, template_name='access.html', context={'course': e})


class AccessCourse(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'access.html'
