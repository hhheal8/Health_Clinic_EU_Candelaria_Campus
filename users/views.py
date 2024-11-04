from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import Group
from django.contrib import messages
from .decorators import admin_required, student_required
from .models import EucUsers, EucStudents, EucHealthClinicInventory

# Actions

def user_login(request):
  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    print(f"Attempting to authenticate user: `{username}`")
    user = authenticate(request, username=username, password=password)
    if user is not None:
      print(f"User `{username}` authenticated successfully")
      login(request, user)
      if user.groups.filter(name="Nurse").exists():
        print(f"User `{username}` belongs to the `Nurse` group")
        return redirect("users:admin_dashboard")
      else:
        print(f"User `{username}` does not belong to the Nurse group")
        return redirect("users:student_basic_information")
    else:
      error_message = "Invalid username or password. Try again."
      print(f"Authentication failed for user: `{username}`")
      return render(request, "index.html", {"error_message": error_message})
    
  return render(request, "index.html")

def user_logout(request):
  logout(request)
  return redirect("index")

# Admin

@admin_required
def admin_dashboard(request):
  total_students = EucStudents.objects.count()
  total_medicines = EucHealthClinicInventory.objects.filter(medicine__isnull=False).count()
  total_equipments = EucHealthClinicInventory.objects.filter(equipment__isnull=False).count()

  context = {
    "total_students": total_students,
    "total_medicines": total_medicines,
    "total_equipments": total_equipments
  }

  return render(request, "users/admin/dashboard.html", context)

@admin_required
def admin_inventory(request):
  if request.method == "POST":
    form_type = request.POST.get("form_type")

    if form_type == "equipment":
      equipment_name = request.POST.get("equipment")
      equipment_total = request.POST.get("total_equipment")

      EucHealthClinicInventory.objects.create(
        user=request.user,
        equipment=equipment_name,
        total_equipment=equipment_total
      )

    elif form_type == "medicine":
      medicine_name = request.POST.get("medicine")
      medicine_total = request.POST.get("total_medicine")

      EucHealthClinicInventory.objects.create(
        user=request.user,
        medicine=medicine_name,
        total_medicine=medicine_total
      )
    
    return redirect("users:admin_inventory")

  equipment_lists = EucHealthClinicInventory.objects.filter(equipment__isnull=False)
  medicine_lists = EucHealthClinicInventory.objects.filter(medicine__isnull=False)

  context = {
    "equipment_lists": equipment_lists,
    "medicine_lists": medicine_lists
  }

  return render(request, "users/admin/inventory.html", context)

@admin_required
def admin_student_log_visit(request):

  context = {}

  return render(request, "users/admin/student_log_visit.html", context)

# Student

@student_required
def student_basic_information(request):

  context = {}

  return render(request, "users/student/basic_information.html", context)

@student_required
def student_physical_examination(request):

  context = {}

  return render(request, "users/student/physical_examination.html", context)

# Actions

