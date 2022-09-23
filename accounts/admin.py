from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

# Register your models here.
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None, {
                "classes":('Wide'),
                "fields":("email", "username", "password1", "password2")
            }
        )
    )
admin.site.register(get_user_model(), UserAdmin)