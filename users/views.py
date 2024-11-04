from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import Group
from django.contrib import messages
from .decorators import admin_required, student_required, login_required_custom

# Actions

# def user_login(request):
#   if request.method == "POST":
#     username = request.POST.get("username")
#     password = request.POST.get("password")
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#       login(request, user)
#       if user.groups.filter(name="Nurse").exists():
#         print("User belongs to Nurse group")
#         return redirect("users:admin_dashboard")
#       else:
#         print("User does not belong to Nurse group")
#         return redirect("users:student_basic_information")
#     else:
#       error_message = "Invalid `username` or `password`. Try again."
#       print("Authentication failed")
#       return render(request, "index.html", {"error_message": error_message})
    
#   return render(request, "index.html")

def user_login(request):
  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    print(f"Attempting to authenticate user: {username}")
    user = authenticate(request, username=username, password=password)
    if user is not None:
      print(f"User {username} authenticated successfully")
      login(request, user)
      if user.groups.filter(name="Nurse").exists():
        print(f"User {username} belongs to the Nurse group")
        return redirect("users:admin_dashboard")
      else:
        print(f"User {username} does not belong to the Nurse group")
        return redirect("users:student_basic_information")
    else:
      error_message = "Invalid username or password. Try again."
      print(f"Authentication failed for user: {username}")
      return render(request, "index.html", {"error_message": error_message})
    
  return render(request, "index.html")

def user_logout(request):
  logout(request)
  return redirect("index")

# Admin

@login_required_custom
@admin_required
def admin_dashboard(request):
  context = {}

  return render(request, "users/admin/dashboard.html", context)

@login_required_custom
@admin_required
def admin_inventory(request):
  context = {}

  return render(request, "users/admin/inventory.html", context)

@login_required_custom
@admin_required
def admin_student_log_visit(request):
  context = {}

  return render(request, "users/admin/student_log_visit.html", context)

# Student

@login_required_custom
@student_required
def student_basic_information(request):
  context = {}

  return render(request, "users/student/basic_information.html", context)

@login_required_custom
@student_required
def student_physical_examination(request):
  context = {}

  return render(request, "users/student/physical_examination.html", context)

# Actions

