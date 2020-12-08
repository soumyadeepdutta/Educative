from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('first_name', 'last_name', 'last_login', 'email', 'password', 'is_teacher')
    list_display = ('email', 'is_staff', 'is_superuser', 'is_teacher')
    


admin.site.register(User, UserAdmin)