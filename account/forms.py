from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Student


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=120)
    last_name = forms.CharField(max_length=120)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('phone',)
