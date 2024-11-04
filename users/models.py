from django.db import models
from django.contrib.auth.models import AbstractUser

class EucUsers(AbstractUser):

  SEX_CHOICES = (
    ("default", "Choose not to say"),
    ("male", "Male"),
    ("female", "Female")
  )

  # Student Basic Information
  middle_name = models.CharField(max_length=50, null=False, blank=False)
  age = models.IntegerField(null=False, blank=False, default=0)
  sex = models.CharField(max_length=20, choices=SEX_CHOICES, null=True, blank=True)
  date_of_exam = models.DateField(null=True, blank=True)
  address = models.CharField(max_length=150, null=True, blank=True)
  date_of_birth = models.DateField(null=True, blank=True)
  contact_number = models.IntegerField(null=True, blank=True)
  status = models.CharField(max_length=50, null=True, blank=True)
  fathers_name = models.CharField(max_length=50, null=True, blank=True)
  fathers_contact = models.IntegerField(null=True, blank=True)
  fathers_occupation = models.CharField(max_length=150, null=True, blank=True)
  mothers_name = models.CharField(max_length=50, null=True, blank=True)
  mothers_contact = models.IntegerField(null=True, blank=True)
  mothers_occupation = models.CharField(max_length=150, null=True, blank=True)
  medical_history = models.CharField(max_length=255, null=True, blank=True)
  
  # Student Physical Examination
  height = models.CharField(max_length=30, null=True, blank=True)
  weight = models.CharField(max_length=30, null=True, blank=True)
  bmi = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
  eyes_vision_right = models.CharField(max_length=50, null=True, blank=True)
  eyes_vision_left = models.CharField(max_length=50, null=True, blank=True)
  ears_vision_right = models.CharField(max_length=50, null=True, blank=True)
  ears_vision_left = models.CharField(max_length=50, null=True, blank=True)
  skin = models.CharField(max_length=50, null=True, blank=True)
  mouth = models.CharField(max_length=50, null=True, blank=True)
  nose = models.CharField(max_length=50, null=True, blank=True)
  bp = models.CharField(max_length=50, null=True, blank=True)
  rate = models.CharField(max_length=50, null=True, blank=True)
  lungs = models.CharField(max_length=50, null=True, blank=True)
  abdomen = models.CharField(max_length=50, null=True, blank=True)
  remarks = models.CharField(max_length=255, null=True, blank=True)

  @property
  def full_name(self):
    return f"{self.first_name} {self.middle_name or ''} {self.last_name}"

  def __str__(self):
    return self.username