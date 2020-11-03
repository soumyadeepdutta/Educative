# from django.contrib.auth.forms import UserCreationForm
# from django.http import HttpResponse
# from django.views.generic import CreateView
# from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import RegisterForm, StudentRegisterForm


# need to be fixed
# class StudentSignupView(CreateView):
#     form_classes = {
#         'register': RegisterForm,
#         'student': StudentRegisterForm
#     }
#     template_name = 'register.html'
#     success_url = reverse_lazy('course:home')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        student = StudentRegisterForm(request.POST)

        if form.is_valid() and student.is_valid():
            user = form.save()
            student_user = student.save(commit=False)  # don't save in db
            student_user.user = user  # for the one to one key
            student_user.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)

            redirect('course:home')
    else:
        form = RegisterForm()
        student_form = StudentRegisterForm()
        context = {'form': form, 'student_form': student_form}
        return render(request, 'register.html', context)
