from django.urls import path, include
from django.contrib import admin
from . import views

app_name = "users"

urlpatterns = [
  path("admin_dashboard/medical_report", views.admin_medical_report, name="admin_medical_report")
]
