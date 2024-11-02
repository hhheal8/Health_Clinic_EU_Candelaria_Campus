from django.urls import path, include
from django.contrib import admin
from . import views

app_name = "users"

urlpatterns = [
  path("admin/dashboard", views.admin_dashboard, name="admin_dashboard"),
  path("admin/student_log_visit", views.admin_student_log_visit, name="admin_student_log_visit"),

  path("student/basic_information", views.student_basic_information, name="student_basic_information"),
  path("student/physical_examination", views.student_physical_examination, name="student_physical_examination")
]
