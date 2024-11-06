from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .decorators import admin_required, student_required
from .models import EucUsers, EucStudents, EucHealthClinicInventory
from django.db.models import Sum
from datetime import datetime

# Actions

def user_login(request):
  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    print(f"Attempting to authenticate user: `{username}`")

    username = username.strip()
    password = password.strip()

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

      # Additional checks
      try:
        user_check = EucUsers.objects.get(username=username)
        print("Check if the user is_active: ", user_check.is_active)
        print("Check if the user is_staff: ", user_check.is_staff)
      except EucUsers.DoesNotExist:
        print("User does not exist")

      return render(request, "index.html", {"error_message": error_message})

  return render(request, "index.html")

def user_logout(request):
  logout(request)
  return redirect("index")

# Admin

@admin_required
def admin_dashboard(request):
  total_students = EucStudents.objects.count() 
  total_medicines = EucHealthClinicInventory.objects.aggregate(Sum('total_medicine'))['total_medicine__sum'] or 0 
  total_equipments = EucHealthClinicInventory.objects.aggregate(Sum('total_equipment'))['total_equipment__sum'] or 0

  context = {
    "total_students": total_students,
    "total_medicines": total_medicines,
    "total_equipments": total_equipments
  }

  return render(request, "users/admin/dashboard.html", context)

# Do not delete
# @admin_required
# def admin_inventory(request):
#   if request.method == "POST":
#     form_type = request.POST.get("form_type")

#     if form_type == "equipment":
#       equipment_name = request.POST.get("equipment")
#       equipment_total = request.POST.get("total_equipment")

#       EucHealthClinicInventory.objects.create(
#         user=request.user,
#         equipment=equipment_name,
#         total_equipment=equipment_total
#       )

#     elif form_type == "medicine":
#       medicine_name = request.POST.get("medicine")
#       medicine_total = request.POST.get("total_medicine")

#       EucHealthClinicInventory.objects.create(
#         user=request.user,
#         medicine=medicine_name,
#         total_medicine=medicine_total
#       )
    
#     return redirect("users:admin_inventory")

#   equipment_lists = EucHealthClinicInventory.objects.filter(equipment__isnull=False)
#   medicine_lists = EucHealthClinicInventory.objects.filter(medicine__isnull=False)

#   context = {
#     "equipment_lists": equipment_lists,
#     "medicine_lists": medicine_lists
#   }

#   return render(request, "users/admin/inventory.html", context)

@admin_required
def admin_inventory(request):
  if request.method == "POST":
    form_type = request.POST.get("form_type")

    if form_type == "equipment":
      equipment_name = request.POST.get("equipment")
      equipment_total = request.POST.get("total_equipment")

      inventory, created = EucHealthClinicInventory.objects.update_or_create(
        equipment=equipment_name,
        defaults={
          'total_equipment': equipment_total,
          'user': request.user
        }
      )
      if created:
        messages.success(request, "New equipment added.")
      else:
        messages.success(request, "Equipment updated.")

    elif form_type == "medicine":
      medicine_name = request.POST.get("medicine")
      medicine_total = request.POST.get("total_medicine")

      inventory, created = EucHealthClinicInventory.objects.update_or_create(
        medicine=medicine_name,
        defaults={
          'total_medicine': medicine_total,
          'user': request.user
        }
      )
      if created:
        messages.success(request, "New medicine added.")
      else:
        messages.success(request, "Medicine updated.")

    return redirect("users:admin_inventory")

  equipment_lists = EucHealthClinicInventory.objects.filter(equipment__isnull=False)
  medicine_lists = EucHealthClinicInventory.objects.filter(medicine__isnull=False)

  context = {
    "equipment_lists": equipment_lists,
    "medicine_lists": medicine_lists
  }

  return render(request, "users/admin/inventory.html", context)

# Do not delete
# @admin_required
# def admin_student_log_visit(request):
#   if request.method == "POST":
#     student_full_name = request.POST.get("student_name")
#     course = request.POST.get("course")
#     year_level = request.POST.get("year_level")
#     medicine_treatment = request.POST.get("medicine_treatment")
#     reason = request.POST.get("reason")
#     date_of_visit = request.POST.get("date_of_visit")

#     name_parts = student_full_name.split()

#     if len(name_parts) == 2:
#       first_name, last_name = name_parts
#       middle_name = ""
#     elif len(name_parts) == 3:
#       first_name, middle_name, last_name = name_parts
#     else:
#       messages.error(request,  "Please enter a valid full name (First Name, Middle Name, and Last Name)")
#       return redirect("users:admin_student_log_visit")
    
#     user, created = EucUsers.objects.get_or_create(
#       first_name=first_name,
#       middle_name=middle_name,
#       last_name=last_name,
#       defaults={"username": first_name + middle_name + last_name}
#     )
#     if created:
#       messages.success(request, "New user created successfully.")
#     else:
#       messages.success(request, "User found and used.")

#     EucStudents.objects.create(
#       user=user,
#       course=course,
#       year_level=year_level,
#       medicine_treatment=medicine_treatment,
#       reason=reason,
#       date_of_visit=date_of_visit
#     )

#     return redirect("users:admin_student_log_visit")
  
#   students = EucStudents.objects.all()

#   context = {
#     "students": students
#   }

#   return render(request, "users/admin/student_log_visit.html", context)

@admin_required
def admin_student_log_visit(request):
  if request.method == "POST":
    student_full_name = request.POST.get("student_name")
    course = request.POST.get("course")
    year_level = request.POST.get("year_level")
    medicine_treatment = request.POST.get("medicine_treatment")
    reason = request.POST.get("reason")
    date_of_visit = request.POST.get("date_of_visit")

    name_parts = student_full_name.split()

    if len(name_parts) == 2:
      first_name, last_name = name_parts
      middle_name = ""
    elif len(name_parts) == 3:
      first_name, middle_name, last_name = name_parts
    else:
      messages.error(request, "Please enter a valid full name (First Name, Middle Name, and Last Name)")
      return redirect("users:admin_student_log_visit")

    user, created = EucUsers.objects.get_or_create(
      first_name=first_name,
      middle_name=middle_name,
      last_name=last_name,
      defaults={"username": first_name + middle_name + last_name}
    )
    if created:
      messages.success(request, "New user created successfully.")
    else:
      messages.success(request, "User found and used.")

    # Check if the student already exists
    student, created = EucStudents.objects.update_or_create(
      user=user,
      defaults={
        "course": course,
        "year_level": year_level,
        "medicine_treatment": medicine_treatment,
        "reason": reason,
        "date_of_visit": date_of_visit
      }
    )

    if created:
      messages.success(request, "Student log visit created successfully.")
    else:
      messages.success(request, "Student log visit updated successfully.")

    return redirect("users:admin_student_log_visit")

  students = EucStudents.objects.all()

  context = {
    "students": students
  }

  return render(request, "users/admin/student_log_visit.html", context)

# Student

@student_required
def student_basic_information(request):
  if request.method == "POST":
    first_name = request.POST.get("first_name")
    middle_name = request.POST.get("middle_name")
    last_name = request.POST.get("last_name")
    age = request.POST.get("age")
    sex = request.POST.get("sex")
    date_of_exam = request.POST.get("date_of_exam") or None
    address = request.POST.get("address")
    date_of_birth = request.POST.get("date_of_birth") or None
    contact_number = request.POST.get("contact_number")
    status = request.POST.get("status")
    fathers_name = request.POST.get("fathers_name")
    fathers_contact = request.POST.get("fathers_contact")
    fathers_occupation = request.POST.get("fathers_occupation")
    mothers_name = request.POST.get("mothers_name")
    mothers_contact = request.POST.get("mothers_contact")
    mothers_occupation = request.POST.get("mothers_occupation")
    medical_history = request.POST.get("medical_history")

    user = request.user

    user.first_name = first_name
    user.middle_name = middle_name
    user.last_name = last_name
    user.save()

    date_of_exam = datetime.strptime(date_of_exam, "%Y-%m-%d").date() if date_of_exam else None
    date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date() if date_of_birth else None

    EucStudents.objects.update_or_create(
      user=user,
      defaults={
        "age": age,
        "sex": sex,
        "date_of_exam": date_of_exam,
        "address": address,
        "date_of_birth": date_of_birth,
        "contact_number": contact_number,
        "status": status,
        "fathers_name": fathers_name,
        "fathers_contact": fathers_contact,
        "fathers_occupation": fathers_occupation,
        "mothers_name": mothers_name,
        "mothers_contact": mothers_contact,
        "mothers_occupation": mothers_occupation,
        "medical_history": medical_history
      }
    )

    return redirect("users:student_physical_examination")

  context = {}

  return render(request, "users/student/basic_information.html", context)

@student_required
def student_physical_examination(request):
  user = request.user
  student = get_object_or_404(EucStudents, user=user)

  if request.method == "POST":
    height = request.POST.get("height")
    weight = request.POST.get("weight")
    bmi = request.POST.get("bmi")
    eyes_vision_right = request.POST.get("eyes_vision_right")
    eyes_vision_left = request.POST.get("eyes_vision_left")
    ears_vision_right = request.POST.get("ears_vision_right")
    ears_vision_left = request.POST.get("ears_vision_left")
    skin = request.POST.get("skin")
    mouth = request.POST.get("mouth")
    nose = request.POST.get("nose")
    bp = request.POST.get("bp")
    rate = request.POST.get("rate")
    lungs = request.POST.get("lungs")
    abdomen = request.POST.get("abdomen")
    remarks = request.POST.get("remarks")

    EucStudents.objects.filter(user=user).update(
      height=height or student.height,
      weight=weight or student.weight,
      bmi=bmi or student.bmi,
      eyes_vision_right=eyes_vision_right or student.eyes_vision_right,
      eyes_vision_left=eyes_vision_left or student.eyes_vision_left,
      ears_vision_right=ears_vision_right or student.ears_vision_right,
      ears_vision_left=ears_vision_left or student.ears_vision_left,
      skin=skin or student.skin,
      mouth=mouth or student.mouth,
      nose=nose or student.nose,
      bp=bp or student.bp,
      rate=rate or student.rate,
      lungs=lungs or student.lungs,
      abdomen=abdomen or student.abdomen,
      remarks=remarks or student.remarks
    )

    return redirect("users:student_physical_examination")

  context = {
    "student": student
  }

  return render(request, "users/student/physical_examination.html", context)


