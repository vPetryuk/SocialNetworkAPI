from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models
from .models import photos, NewUser


# Register your models here.

admin.site.register(photos)


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'user_name',)
    list_filter = ('email', 'user_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'user_name',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'password','photos')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'password1', 'password2', 'is_active', 'is_staff', 'photos')}
         ),
    )


admin.site.register(NewUser,UserAdminConfig)