from django.shortcuts import render
from rest_framework import generics
from .models import Students
from .serializers import StudentsSerializers

# Create your views here.

class StudentListView(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializers

