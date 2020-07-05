from django import forms
from .models import Students
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Students
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Students
        fields = UserChangeForm.Meta.fields


#
# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Students
#         fields='__all__'
