from rest_framework import serializers
from .models import Students

class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Students
        fields=['is_staff','is_active','is_superuser','username','password','last_login','date_joined','profile','fullname','email','gender','birthdate','semester','department','enrollment','lastsemspi','lastsemcpi']


