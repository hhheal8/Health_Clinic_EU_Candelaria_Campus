from django import forms
from django.forms.widgets import PasswordInput
from django.core.exceptions import ValidationError
from .models import EucUsers, EucStudents, EucHealthClinicInventory

class EucUsersForm(forms.ModelForm):

  class Meta:
    model = EucUsers
    fields = [
      "first_name", "middle_name", 
      "last_name", "email"
    ]


class EucStudentsForm(forms.ModelForm):

  class Meta:
    model = EucStudents
    fields = [
      # Basic Information
      "age", "sex", "date_of_exam", "address", "date_of_birth", 
      "contact_number", "status", "fathers_name", "fathers_occupation", "mothers_name", 
      "mothers_contact", "mothers_occupation", "medical_history", 

      # Physical Examination
      "height", "weight", "bmi", "eyes_vision_right", "eyes_vision_left", 
      "ears_vision_right", "ears_vision_left", "skin", "mouth", "nose", 
      "bp", "rate", "lungs", "abdomen", "remarks", 
      "course", "year_level", "medicine_treatment", "reason", "date_of_visit"
    ]

class EucHealthClinicInventoryForm(forms.ModelForm):

  class Meta:
    model = EucHealthClinicInventory
    fields = [
      "equipment", "total_equipment", "medicine", "total_medicine"
    ]