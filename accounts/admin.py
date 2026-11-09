

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'email', 'xp_balance', 'matches_played', 'matches_won', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('id',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Game Stats', {'fields': ('xp_balance', 'matches_played', 'matches_won')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )