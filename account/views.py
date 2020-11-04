from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views import View
from django.contrib.auth.views import AuthenticationForm


class RegistrationView(CreateView):
    form_class = UserCreationForm
    # model = User
    template_name = 'register.html'
    print('registered')
    success_url = reverse_lazy('course:courseList')
    # fields = ('username', 'password1')


class LoginView(View):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('course:courseList')
