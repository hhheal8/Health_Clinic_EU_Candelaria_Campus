from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def admin_medical_report(request):
  context = {}
  return render(request, "users/admin/medical_report.html", context)
