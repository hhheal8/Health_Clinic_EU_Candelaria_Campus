from django.contrib import admin
from .models import EucUsers, EucStudents

# from django.contrib.auth.admin import UserAdmin --- default
# admin.site.register(EucUsers, UserAdmin) --- default

# Register your models here.

@admin.register(EucUsers)
class EucUsersAdmin(admin.ModelAdmin):
  list_display = ("username", "first_name", "last_name", "email", "is_staff", "is_superuser")
  search_fileds = ("username", "first_name", "last_name", "email")
  list_filter = ("is_staff", "is_superuser")
  ordering = ("username", )
  filter_horizontal = ("groups", "user_permissions")

@admin.register(EucStudents)
class EucStudentsAdmin(admin.ModelAdmin):
  list_display = ("user", "age", "course", "year_level", "date_of_exam")
  search_fileds = ("user__username", "user__full_name", "user__first_name", "user__last_name")
  list_filter = ("course", "year_level")
  ordering = ("user", )