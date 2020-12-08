# from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .forms import SignupForm


# Create your views here.
class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'login.html'
    success_url = reverse_lazy('accounts:profile')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["auth"] = 'Signup'
        return context
    

class ProfileView(TemplateView):
    model = get_user_model()
    template_name = 'profile.html'

