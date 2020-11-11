from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import RegisterView, ProfileView

app_name = 'account'
urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout', login_required(LogoutView.as_view()), name='logout'),
    path('profile/<str:pk>', ProfileView.as_view(), name='profile')
]
