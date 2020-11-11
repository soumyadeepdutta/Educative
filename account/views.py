from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import RegistrationForm
from django.contrib.auth import get_user_model


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('account:login')
    success_message = 'Profile created successfully'


class ProfileView(DetailView):
    model = get_user_model()
    template_name = 'profile.html'
    slug_field = 'email'
    context_object_name = 'profile'
