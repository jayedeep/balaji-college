from django.contrib import admin
from .models import Students,PreviousMarks
# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = Students
    list_display = ['email', 'username', 'fullname']

admin.site.register(Students, CustomUserAdmin)
admin.site.register(PreviousMarks)
