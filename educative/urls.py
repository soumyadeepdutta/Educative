from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('course.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('account.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
