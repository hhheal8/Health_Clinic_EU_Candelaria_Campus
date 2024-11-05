from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import EucUsers, EucStudents

# from django.contrib.auth.admin import UserAdmin --- default
# admin.site.register(EucUsers, UserAdmin) --- default

# Register your models here.

@admin.register(EucUsers)
class EucUsersAdmin(UserAdmin):
  list_display = ("username", "first_name", "last_name", "email", "is_staff", "is_superuser")
  search_fileds = ("username", "first_name", "last_name", "email")
  list_filter = ("is_staff", "is_superuser")
  ordering = ("username", )
  filter_horizontal = ("groups", "user_permissions")
  fieldsets = (
    (None, {"fields": ("username", "password")}),
    ("Personal Information", {"fields": ("first_name", "middle_name", "last_name", "email")}),
    ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")})
  )
  add_fieldsets = (
    (None, {
      "classes": ("wide", ),
      "fields": ("username", "first_name", "middle_name", "last_name", "email", "password1", "password2", "is_staff", "groups")
    }),
  )

@admin.register(EucStudents)
class EucStudentsAdmin(admin.ModelAdmin):
  list_display = ("user", "age", "course", "year_level", "date_of_exam")
  search_fileds = ("user__username", "user__full_name", "user__first_name", "user__last_name")
  list_filter = ("course", "year_level")
  ordering = ("user", )

  def has_change_permission(self, request, obj=None):
    if request.user.groups.filter(name="Nurse").exists() or request.user.is_superuser:
      return True
    return False
  
  def has_delete_permission(self, request, obj=None):
    if request.user.groups.filter(name="Nurse").exists() or request.user.is_superuser:
      return True
    return False