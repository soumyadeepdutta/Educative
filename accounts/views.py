from django.shortcuts import render
from course.models import Enrollment
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignupForm


# Create your views here.
class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'register.html'
    success_url = reverse_lazy('accounts:profile')


def profile(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, template_name='profile.html', context={'enrollments': enrollments})
