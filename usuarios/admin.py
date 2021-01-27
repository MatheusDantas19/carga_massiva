from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .forms import UserChangeForm, UserCreationForm

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    # form = UserChangeForm
    # add_form = UserCreationForm
    model = Usuario
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Campos personalizados", {'fields': ('bio', )}),
    )

admin.site.register(Usuario, UserAdmin)
