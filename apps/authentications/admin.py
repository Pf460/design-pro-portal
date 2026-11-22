from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserManager

User=get_user_model()

@admin.register(User)
class UserAdmin(BaseUserManager):
    list_display = ['id', 'username', 'email', 'fio', 'is_staff', 'is_superuser']
    list_filter = ['is_staff', 'is_superuser']
    search_fields = ['username', 'email', 'fio']

    fieldsets = (
        (None, {'fields': ('username', 'email', 'fio', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
