from django.urls import path, include
from django.contrib import admin
from . import views

app_name = "users"

urlpatterns = [
  path("student/basic_information", views.student_basic_information, name="student_basic_information"),
  path("student/physical_examination", views.student_physical_examination, name="student_physical_examination")
]
