from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

def login_required_custom(view_fun):
  def _wrapped_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
      print("User not authenticated. Redirecting to index.")
      return redirect('index')  
    return view_fun(request, *args, **kwargs)
  return _wrapped_view

def admin_required(view_fun):
  @wraps(view_fun)
  def _wrapped_view(request, *args, **kwargs):
    if not request.user.is_authenticated or not request.user.is_staff:
      print("User not authorized. Returning forbidden response.")
      # return HttpResponseForbidden("You are not allowed to access this page.")
      return redirect('index')  
    return view_fun(request, *args, **kwargs)
  return _wrapped_view

def student_required(view_fun):
  @wraps(view_fun)
  def _wrapped_view(request, *args, **kwargs):
    if not request.user.is_authenticated or request.user.is_staff:
      print("User not authorized. Returning forbidden response.")
      # return HttpResponseForbidden("You are not allowed to access this page.")
      return redirect('index')  
    return view_fun(request, *args, **kwargs)
  return _wrapped_view
