from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from App_login.models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['pk', 'first_name', 'last_name', 'email', 'username']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'picture')}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'picture')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
