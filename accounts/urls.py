from django.urls import path
from .views import SignupView, profile
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

app_name = 'accounts'
urlpatterns = [
    path('signup/', SignupView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path("profile/", profile, name="profile")
]
