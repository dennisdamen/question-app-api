from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext as _
from django import forms
from django.contrib import admin

from .models import User


class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            get_user_model().objects.get(username=username)
        except get_user_model().DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    fieldsets = (
        (None, {'fields': [('username', 'password'),]}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                   'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        )


admin.site.register(User, MyUserAdmin)