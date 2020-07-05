from django.urls import include,path

from . import views

urlpatterns=[
    path('',views.StudentListView.as_view()),
]