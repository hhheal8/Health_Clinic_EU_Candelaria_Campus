from django.urls import path, include
from django.contrib import admin
from . import views

app_name = "users"

urlpatterns = [
  path("login", views.user_login, name="user_login"),
  path("logout", views.user_logout, name="user_logout"),

  path("admin/dashboard", views.admin_dashboard, name="admin_dashboard"),
  path("admin/inventory", views.admin_inventory, name="admin_inventory"),
  path("admin/student_log_visit", views.admin_student_log_visit, name="admin_student_log_visit"),

  path("student/basic_information", views.student_basic_information, name="student_basic_information"),
  path("student/physical_examination", views.student_physical_examination, name="student_physical_examination")
]
