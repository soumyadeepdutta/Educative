from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'account'
urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='registerStudent'),
    path('login-user/', LoginView.as_view(template_name='login.html'), name='loginStudent')
]
